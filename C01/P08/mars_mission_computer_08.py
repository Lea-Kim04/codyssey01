import sys
import time
import json
import keyboard
import importlib.util
import platform  #system info 
import psutil #HW resource info

sys.path.append('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P06')

def load_dummy_sensor():
    module_path = 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P06\\mars_mission_computer_P06.py'
    spec = importlib.util.spec_from_file_location("mars_mission_computer_P06", module_path)
    #print (spec)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.DummySensor

try:
    
    class MissionComputer:

        def __init__(self):
            self.env_values = {'mars_base_internal_temperature' : [], 'mars_base_external_temperature' : [],
                'mars_base_internal_humidity' : [], 'mars_base_external_illuminance' : [],
                'mars_base_internal_co2' : [],'mars_base_internal_oxygen' : []}
            
            DummySensor = load_dummy_sensor()
            self.ds = DummySensor()
        

        def get_sensor_data(self):
            count = 1
            while(True):
                if stop_flag:
                    break
                self.ds.set_env()
                data = self.ds.get_env() 
                print('index' + str(count))
                print(json.dumps(data, indent = 1, ensure_ascii = False))
                count += 1

                for key in self.env_values:
                    self.env_values[key].append(data[key])
                
                time.sleep(5)

                if count % 12 == 0:
                    RunComputer.averages_5min()
        
        def averages_5min(self):
                print(f"{'-'*10} < 5min_averages > {'-'*10}")
                for key in self.env_values:  
                    values = self.env_values[key][-12:]
                    if values:
                        avg = sum(values) / len(values)
                        print(f'{key} : {avg:.2f}')
                    else: 
                        print(f'Not enough values for the {key}.')
                print(f"{'-'*39}\n)")

        def get_mission_computer_info(self): #08
            self.os_info = {
                '운영체계' : platform.system(), '운영체계 버전' : platform.version(), 
                'CPU 종류' : platform.processor(), 'CPU 코어 수' : psutil.cpu_count(logical=False), 
                '논리 코어 수' : psutil.cpu_count(logical=True),  
                '메모리 크기' : f'{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB'}
            
            with open('os_info', 'w', encoding = 'utf-8') as file1:
                json.dump(self.os_info, file1, ensure_ascii=False) #save as Json file
                print('-'*8, 'JSON FILE_os', '-'*8)
                #print(json.dumps(self.os_info, ensure_ascii=False, indent=1)) #확인용 출력
                return self.os_info

        def get_mission_computer_load(self): #08
            self.hw_info = {
                'CPU 실시간 사용량' : f'{psutil.cpu_percent(interval=1)} %',
                '메모리 실시간 사용량' : f'{psutil.virtual_memory().percent} %'}

            with open('hw_info', 'w', encoding = 'utf-8') as file2:
                json.dump(self.hw_info, file2, ensure_ascii=False)
                print('-'*8, 'JSON FILE_hw', '-'*8) #save as Json file
                #print(json.dumps(self.hw_info, ensure_ascii=False, indent=1)) #확인용 출력
                return self.hw_info 
            
    runComputer = MissionComputer()
    print(runComputer.get_mission_computer_info()) #08 호출
    print(runComputer.get_mission_computer_load()) #08 호출

    stop_flag = False 
    def stop_program():
        global stop_flag
        print('System stopped…') 
        stop_flag = True

    keyboard.add_hotkey('q', stop_program) 

    RunComputer = MissionComputer()
    RunComputer.get_sensor_data()

except FileNotFoundError: 
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)