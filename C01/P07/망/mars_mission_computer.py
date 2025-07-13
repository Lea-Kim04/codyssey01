import time
import json

def check_stop(value: str):
    if value == 'q':
        print('Sytem stoped…')
        return True #stop
    return False

try:
    from mars_dummy_sensor import DummySensor
    
    class MissionComputer:

        def __init__(self):
            self.env_values = {}
            self.sensor = DummySensor() 

        def get_sensor_data(self):
            while True:
                self.sensor.update()
                self.env_values['internal_temperature'] = self.sensor.mars_base_internal_temperature #1
                self.env_values['external_temperature'] = self.sensor.mars_base_external_temperature
                self.env_values['internal_humidity'] = self.sensor.mars_base_internal_humidity 
                self.env_values['external_illuminance'] = self.sensor.mars_base_external_illuminance
                self.env_values['internal_co2'] = self.sensor.mars_base_internal_co2 
                self.env_values['internal_oxygen'] = self.sensor.mars_base_internal_oxygen

                print(json.dumps(self.env_values, None)) #2
                time.sleep(5) #*5
                
                user_input = input('Enter input (type "q" to quit): ')
                if check_stop(user_input):  # True - stop
                    break
                print('Continuing to load data...')

        def averages(self):
            print("\n--- 5분 평균값 ---")
            for key in self.time_history:
                values = self.time_history[key][-60:]  # 최근 60개만 사용 (5초마다 저장 × 60 = 5분)
                if values:
                    avg = sum(values) / len(values)
                    print(f"{key}: {avg:.2f}")
                            
    ds = DummySensor()  
    RunComputer = MissionComputer()

    while True:
        RunComputer.get_sensor_data()
        time.sleep(5)   
        input_massage = input('Continue? (type "q" to quit):')
        if check_stop(input_massage):
            break
        print('Continuing to load data...')

except FileNotFoundError: 
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)

