import json

arr = []

try:
    with open ('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P02\\mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        next(file1)
        file2 = file1.readlines()
#분류 및 list 객체전환
        for line in file2:
            timestamp, event, message = line.split(',')
            date, time = timestamp.split(' ')
            arr.append([date, time, event, message])

#전환된 list 객체를 화면에 출력
    for info in arr:
          print(info)


    print("-------- 구   분 -------")
# list 객체를 시간의 역순으로 정렬
    new_arr = sorted(arr, reverse=True)
# list 객체를 dict 객체로 전환
    arr_dict = {}
    for date, time, event, message in new_arr:
        key = date + ' ' + time
        message = message.strip()
        arr_dict[key] = {'event' : event, 'message' : message}

#Create JSON
    with open('mission_computer_main.json', 'w', encoding = 'utf-8') as file3:
                    json.dump(arr_dict,file3,ensure_ascii=False,indent=4)
#Read JSON
    with open('mission_computer_main.json', 'r', encoding = 'utf-8') as file3:
            data_loaded = json.load(file3)
#Test JSON
    print('저장 후 읽어온 데이터')
    print(data_loaded)


except FileNotFoundError:
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)