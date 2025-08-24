import sys
import time
import json
import keyboard
import importlib.util

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
                data = self.ds.get_env() #sensor vlaue
                print('index' + str(count))
                print(json.dumps(data, indent = 1, ensure_ascii = False))
                count += 1

                for key in self.env_values:
                    self.env_values[key].append(data[key])
                
                time.sleep(5)

                if count % 12 == 0:
                    RunComputer.averages_5min()
                
            # return data
        
        def averages_5min(self):
                print(f"{'-'*10} < 5min_averages > {'-'*10}")
                for key in self.env_values:  
                    values = self.env_values[key][-12:] # 5*12 = 60 = 5min
                    if values:
                        avg = sum(values) / len(values)
                        print(f'{key} : {avg:.2f}')
                    else: 
                        print(f'Not enough values for the {key}.')
                print(f"{'-'*39}\n)")

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