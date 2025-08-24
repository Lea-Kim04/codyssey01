import threading

from P07_mission_computer import MissionComputer 
from P08_mission_computer import MissionComputer 

runComputer = MissionComputer()

thread_info = threading.Thread(target=runComputer.get_mission_computer_info)
thread_load = threading.Thread(target=runComputer.get_mission_computer_load)
thread_sensor = threading.Thread(target=runComputer.get_sensor_data)

# 각 쓰레드 실행
thread_info.start()
thread_load.start()
thread_sensor.start()

# 필요시 메인 쓰레드에서 이 쓰레드들이 끝날 때까지 대기 (옵션)
# thread_info.join()
# thread_load.join()
# thread_sensor.join()
