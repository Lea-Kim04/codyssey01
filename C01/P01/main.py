print('Hello Mars')

#전체 리스트 정렬
try:
    with open('C:/Users/jin_y/Downloads/SW camp1/C01/P01/mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        for line in file1:
            print(line.strip())

except:
    print('파일이 열리지 않음')
    exit()


#사고 원인 추출_보너스문제
print('Hello Mars')
try:
    with open('C:/Users/jin_y/Downloads/SW camp1/C01/P01/mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        for line in file1:
            if 'Oxygen tank' in line:
                print(line.strip())

except:
    print('파일이 열리지 않음')
    exit()


#시간의 역순 정렬_보너스문제
try:
    with open('C:/Users/jin_y/Downloads/SW camp1/C01/P01/mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        lines = file1.readlines()
        for line in reversed(lines):
            print(line.strip())

except:
    print('파일이 열리지 않음')
    exit()
