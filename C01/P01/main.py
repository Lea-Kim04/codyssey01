#Hello Mars 출력
print('Hello Mars')

#전체 리스트 정렬
try:
    with open('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P01\\mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        for line in file1:
            print(line.strip())

except FileNotFoundError:
    print('파일을 읽을 수 없음')
    exit()


#사고 원인 추출_보너스문제
print('--- 보너스 문제01 ---')
try:
    with open('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P01\\mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        for line in file1:
            if 'Oxygen tank' in line:
                print(line.strip())

except FileNotFoundError:
    print('파일을 읽을 수 없음')
    exit()


#시간의 역순 정렬_보너스문제
print('--- 보너스 문제02 ---')
try:
    with open('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P01\\mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        lines = file1.readlines()
        for line in reversed(lines):
            print(line.strip())

except FileNotFoundError:
    print('파일을 읽을 수 없음')
    exit()
