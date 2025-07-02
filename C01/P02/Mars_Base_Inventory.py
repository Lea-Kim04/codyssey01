print('기본문제')

arr = list()
try:
    with open('../P01/mission_computer_main.log', 'r', encoding = 'utf-8') as file1:
        file2 = reversed(file1.readlines())
        for line in file2:
            timestamp, event, message = line.split(',')
            date, time = timestamp.split(' ')
            arr.append((date, time, event, message))
            arr.sort(reverse=True)
            print(arr)


            # print("date: ", date)
            # print("time", time)
            # print("event: ", event)
            # print("message: ", message)

except Exception as e:
    print(e)
    exit()