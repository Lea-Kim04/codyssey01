import platform  #system info 
import psutil #HW resource info
import json
import sys
import importlib.util

sys.path.append('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P07')

def load_dummy_sensor():
    module_path = 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P06\\mars_mission_computer_P06.py'
    spec = importlib.util.spec_from_file_location("mars_mission_computer_P06", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.DummySensor

def load_mission_computer():
    module_path = 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P07\\mars_mission_computer_07.py'
    spec = importlib.util.spec_from_file_location("mars_mission_computer_07", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.MissionComputer

try:

    class MissionComputer(load_mission_computer()):
        
        def __init__(self):
            super().__init__()  # 부모 클래스 초기화
            DummySensor = load_dummy_sensor()
            self.ds = DummySensor()

        def get_mission_computer_info(self):
            self.os_info = {
                '운영체계' : platform.system(), '운영체계 버전' : platform.version(), 
                'CPU 종류' : platform.processor(), 'CPU 코어 수' : psutil.cpu_count(logical=False), 
                '논리 코어 수' : psutil.cpu_count(logical=True),  
                '메모리 크기' : f'{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB'}
            
            with open('os_info', 'w', encoding = 'utf-8') as file1:
                json.dump(self.os_info, file1, ensure_ascii=False)
                print('-'*8, 'JSON FILE_os', '-'*8)
                #print(json.dumps(self.os_info, ensure_ascii=False, indent=1))
                return self.os_info

        def get_mission_computer_load(self):
            self.hw_info = {
                'CPU 실시간 사용량' : f'{psutil.cpu_percent(interval=1)} %',
                '메모리 실시간 사용량' : f'{psutil.virtual_memory().percent} %'}

            with open('hw_info', 'w', encoding = 'utf-8') as file2:
                json.dump(self.hw_info, file2, ensure_ascii=False)
                print('-'*8, 'JSON FILE_hw', '-'*8)
                #print(json.dumps(self.hw_info, ensure_ascii=False, indent=1))
                return self.hw_info 
            
    runComputer = MissionComputer() 
    print(runComputer.get_mission_computer_info())
    print(runComputer.get_mission_computer_load())

    DummySensor = load_dummy_sensor()
    RunComputer = DummySensor()

    runComputer.get_sensor_data()
        
except FileNotFoundError: 
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)