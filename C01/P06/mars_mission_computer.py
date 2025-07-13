import random
import datetime

try:
    class DummySensor:

        def __init__(self):
            self.env_values = {}

        def set_env(self):
            self.env_values = {
            'mars_base_internal_temperature' : random.randint(18, 30), 'mars_base_external_temperature' : random.randint(0, 21),
            'mars_base_internal_humidity' : random.randint(50, 60), 'mars_base_external_illuminance' : random.randint(500, 715),
            'mars_base_internal_co2' : random.uniform(0.02, 0.1),'mars_base_internal_oxygen' : random.randint(4, 7)}

        def get_env(self):
            with open('mars_sensor_log.txt', 'a') as f: #log file+
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                env_log = (f'날짜 및 시간 : {now}, '
                    f'내부 온도 : {self.env_values["mars_base_internal_temperature"]}, '
                    f'외부 온도 : {self.env_values["mars_base_external_temperature"]}, '
                    f'내부 습도 : {self.env_values["mars_base_internal_humidity"]}, '
                    f'외부 광량 : {self.env_values["mars_base_external_illuminance"]}, '
                    f'내부 CO2농도 : {self.env_values["mars_base_internal_co2"]:.3f}, '
                    f'내부 O2농도 : {self.env_values["mars_base_internal_oxygen"]}\n')
                f.write(env_log)

                #print(env_log)
                return self.env_values


    ds = DummySensor()

    ds.set_env()
    print(ds.get_env())
    print('mars_sensor_log.txt')
    #save

except FileNotFoundError: 
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)
