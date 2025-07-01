print('Hello Mars')
try:
    with open('C:/Users/jin_y/Downloads/SW camp1/C01/P01/mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        for line in file1:
            if 'Oxygen tank' in line:
                print(line.strip())


except:
    print('파일이 열리지 않음')
    exit()