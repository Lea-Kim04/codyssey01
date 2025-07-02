print('Hello Mars')

print('기본문제')
try:
    with open('C:/Users/jin_y/Downloads/SW camp1/C01/P01/mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        lines = file1.readlines()
        for line in lines:
            print(line.strip())

except:
    print('파일이 열리지 않음')
    exit()

print('시간의 역순_보너스문제')
for line in reversed(lines):
    print(line.strip())
# try:
#     with open('C:/Users/jin_y/Downloads/SW camp1/C01/P01/mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
#         lines = file1.readlines()
#         for line in reversed(lines):
#             print(line.strip())

print('사고 원인 추출_보너스문제')
for line in lines:
    if 'Oxygen tank' in line:
        print(line.strip())
#             if 'Oxygen tank' in line:
#                 print(line.strip())
