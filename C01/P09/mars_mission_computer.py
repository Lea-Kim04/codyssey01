import sys
import time
import json
import importlib.util
import platform
import psutil
import multiprocessing

sys.path.append('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P06')

def load_dummy_sensor():
    module_path = 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P06\\mars_mission_computer_P06.py'
    spec = importlib.util.spec_from_file_location("mars_mission_computer_P06", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.DummySensor

class MissionComputer:

    def __init__(self):
        self.env_values = {'mars_base_internal_temperature': [], 'mars_base_external_temperature': [],
                           'mars_base_internal_humidity': [], 'mars_base_external_illuminance': [],
                           'mars_base_internal_co2': [], 'mars_base_internal_oxygen': []}
        self.stop_flag = multiprocessing.Value('b', False)

    def set_stop_flag(self):
        self.stop_flag.value = True
        print(f"[{multiprocessing.current_process().name}] System stopped…")

    def get_sensor_data(self):
        DummySensor = load_dummy_sensor()
        ds = DummySensor()
        count = 1
        while not self.stop_flag.value:
            ds.set_env()
            data = ds.get_env()
            print(f"[{multiprocessing.current_process().name}] index{count}")
            print(json.dumps(data, indent=1, ensure_ascii=False))
            count += 1

            for key in self.env_values:
                self.env_values[key].append(data[key])

            time.sleep(5)
            if count % 12 == 0:
                self.averages_5min()

    def averages_5min(self):
        print(f"[{multiprocessing.current_process().name}] {'-'*10} < 5min_averages > {'-'*10}")
        for key in self.env_values:
            values = self.env_values[key][-12:]
            if values:
                avg = sum(values) / len(values)
                print(f'{key} : {avg:.2f}')
            else:
                print(f'Not enough values for {key}.')
        print(f"{'-'*39}\n")

    def get_mission_computer_info(self):
        while not self.stop_flag.value:
            os_info = {
                '운영체계': platform.system(),
                '운영체계 버전': platform.version(),
                'CPU 종류': platform.processor(),
                'CPU 코어 수': psutil.cpu_count(logical=False),
                '논리 코어 수': psutil.cpu_count(logical=True),
                '메모리 크기': f'{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB'
            }
            with open('os_info', 'w', encoding='utf-8') as file1:
                json.dump(os_info, file1, ensure_ascii=False)
            print(f"[{multiprocessing.current_process().name}] JSON FILE_os")
            print(os_info)
            time.sleep(20)

    def get_mission_computer_load(self):
        while not self.stop_flag.value:
            hw_info = {
                'CPU 실시간 사용량': f'{psutil.cpu_percent(interval=1)} %',
                '메모리 실시간 사용량': f'{psutil.virtual_memory().percent} %'
            }
            with open('hw_info', 'w', encoding='utf-8') as file2:
                json.dump(hw_info, file2, ensure_ascii=False)
            print(f"[{multiprocessing.current_process().name}] JSON FILE_hw")
            print(hw_info)
            time.sleep(20)

if __name__ == "__main__":
    runComputer1 = MissionComputer()
    runComputer2 = MissionComputer()
    runComputer3 = MissionComputer()

    p1 = multiprocessing.Process(target=runComputer1.get_mission_computer_info, name='runComputer1')
    p2 = multiprocessing.Process(target=runComputer2.get_mission_computer_load, name='runComputer2')
    p3 = multiprocessing.Process(target=runComputer3.get_sensor_data, name='runComputer3')

    p1.start()
    p2.start()
    p3.start()

    try:
        input("Press Enter to stop...\n")
        runComputer1.set_stop_flag()
        runComputer2.set_stop_flag()
        runComputer3.set_stop_flag()
    except KeyboardInterrupt: #Ctrl+C pyhthon내장 예외처리
        runComputer1.set_stop_flag()
        runComputer2.set_stop_flag()
        runComputer3.set_stop_flag()

    p1.join()
    p2.join()
    p3.join()
