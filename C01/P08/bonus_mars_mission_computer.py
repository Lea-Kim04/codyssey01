# setting.txt 파일을 만들어서 
# 출력되는 정보의 항목을 셋팅 할 수 있도록 
# 코드를 수정한다.

import platform 
import psutil
import json

try:
    class MissionComputer:
        def __init__(self):
            self.os_info = {}
            self.hw_info = {}

        def load_settings(self,file_name = 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P08\\setting.txt'):
            with open(file_name, 'r', encoding='utf-8') as file3:
                items = [line.strip() for line in file3 if line.strip()]
            return items

        def get_mission_computer_info(self):
            self.os_info = {
                '운영체계' : platform.system(), '운영체계 버전' : platform.version(), 
                'CPU 종류' : platform.processor(), 'CPU 코어 수' : psutil.cpu_count(logical=False), 
                '논리 코어 수' : psutil.cpu_count(logical=True),  
                '메모리 크기' : f'{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB'}  # 1GB = 1024³ byte
        
            selected_items = self.load_settings()

            setting_os_info = {key : value for key, value in self.os_info.items() if key in selected_items}

            with open('os_info', 'w', encoding = 'utf-8') as file1:
                json.dump(setting_os_info, file1, ensure_ascii=False)
                print('-'*8, 'JSON FILE_os', '-'*8)
                #print(json.dumps(setting_os_info, ensure_ascii=False, indent=1))

                return setting_os_info

        def get_mission_computer_load(self):
            self.hw_info = {
                'CPU 실시간 사용량' : f'{psutil.cpu_percent(interval=1)} %',
                '메모리 실시간 사용량' : f'{psutil.virtual_memory().percent} %'}

            selected_items = self.load_settings()

            setting_hw_info = {key : value for key, value in self.hw_info.items() if key in selected_items}

            with open('hw_info', 'w', encoding = 'utf-8') as file2:
                json.dump(setting_hw_info, file2, ensure_ascii=False)
                print('-'*8, 'JSON FILE_hw', '-'*8)
                #print(json.dumps(setting_hw_info, ensure_ascii=False, indent=1))

                return self.hw_info 
            
    runComputer = MissionComputer()
    print(runComputer.get_mission_computer_info())
    print(runComputer.get_mission_computer_load())

except FileNotFoundError: 
     print('파일이 존재하지 않음.')
except Exception as e:
     print('파일 처리 중 오류가 발생.', e)