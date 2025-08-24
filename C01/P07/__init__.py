import time
import json
import keyboard

from mars_mission_computer import DummySensor

try:
    
    class MissionComputer:

        def __init__(self):
            self.env_values = {'mars_base_internal_temperature' : [], 'mars_base_external_temperature' : [],
                'mars_base_internal_humidity' : [], 'mars_base_external_illuminance' : [],
                'mars_base_internal_co2' : [],'mars_base_internal_oxygen' : []}
            
            self.ds = DummySensor()
        
        def get_sensor_data(self):
            data = self.ds.get_env() #sensor vlaue
            for key, value in data.items():
                if key in self.env_values:
                    self.env_values[key].append(value)
                else:
                    self.env_values[key] = [value]  #new key -> new list
            return data

        def averages_5min(self):
                print(f'{'-'*10} < 5min_averages > {'-'*10}')
                for key in self.env_values:  
                    values = self.env_values[key][-60:] # 5*12 = 60 = 5min
                    if values:
                        avg = sum(values) / len(values)
                        print(f'{key} : {avg:.2f}')
                    else: 
                        print(f'Not enough values for the {key}.')
                print(f'{'-'*39}\n)')


    RunComputer = MissionComputer()

    stop_flag = False 
    def stop_program():
        global stop_flag
        print('System stopped…') 
        stop_flag = True

    keyboard.add_hotkey('q', stop_program) 

    count = 1
    while True:
        if stop_flag:
            break

        print('index' + str(count))
        env_values = RunComputer.get_sensor_data() ## 
        print(json.dumps(env_values, indent = 1, ensure_ascii = False))
        time.sleep(5)
        count += 1
        
        if count % 60 == 0:
            RunComputer.averages_5min() ##
        

except FileNotFoundError: 
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)