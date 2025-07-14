import time
import json
import keyboard

from mars_dummy_sensor import DummySensor

try:
    
    class MissionComputer:

        def __init__(self):
            self.env_values = {'mars_base_internal_temperature' : None, 'mars_base_external_temperature' : None,
                'mars_base_internal_humidity' : None, 'mars_base_external_illuminance' : None,
                'mars_base_internal_co2' : None,'mars_base_internal_oxygen' : None}
            
            self.ds = DummySensor()
        
        def get_sensor_data(self):
            data = self.ds.get_env()
            self.env_values.update(data) #1
            return self.env_values

        def averages_5min(self):
                print('-'*10, 'averages_5min', '-'*10)
                for key in self.env_values:
                    values = self.env_values[key][-60:] #5*12 = 60 = 5min 
                    if values:
                        avg = sum(values) / len(values)
                        print(f"{key}: {avg:.2f}")
            

    RunComputer = MissionComputer()

    stop_flag = False #변수
    def stop_program():
        global stop_flag
        print('System stopped…') 
        stop_flag = True

    keyboard.add_hotkey('q', stop_program)

    while True:
        if stop_flag:
            break

        env_values = RunComputer.get_sensor_data()
        print(json.dumps(env_values, indent = 1, ensure_ascii = False)) #2
        time.sleep(5)
        

except FileNotFoundError: 
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)