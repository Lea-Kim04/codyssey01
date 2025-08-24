import numpy as np 
try: 
    main_path = (['C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P05\\mars_base_main_parts-001.csv', 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P05\\mars_base_main_parts-002.csv', 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P05\\mars_base_main_parts-003.csv'])
    main_list = []

    a1 = np.genfromtxt(main_path[0], delimiter=',', skip_header = 1, dtype=None, encoding = 'utf-8') #dtype = 타입 자동추정
    a2 = np.genfromtxt(main_path[1], delimiter=',', skip_header = 1, dtype=None, encoding = 'utf-8') #genfromtxt. 결측값 허용 문자열 허용
    a3 = np.genfromtxt(main_path[2], delimiter=',', skip_header = 1, dtype=None, encoding = 'utf-8')

    merge_a = np.vstack((a1,a2,a3)) #배열 쌓기

    parts = np.unique(merge_a['f0']) #ndarray
    for name in parts: 
        strength_values = merge_a['f1'][merge_a['f0'] == name] # original
        # print(f"{name}: {strength_values}")

    avg_list = [] # FL < 50
    for name in parts:
        strength_values = merge_a['f1'][merge_a['f0'] == name]
        avg = np.mean(strength_values)
        if avg < 50:
            avg_list.append((name, round(avg, 1)))

    avg_array = np.array(avg_list)
    # print(avg_array) 
    np.savetxt('parts_to_work_on.csv', avg_array, delimiter = ',', fmt = '%s') #save as csv.(FL < 50)

except FileNotFoundError: 
    print('File not found.')
except Exception as e:
    print('An error occurred:', e)

print('-'*8, 'transpose', '-'*8)

try:
    parts2 = np.loadtxt('C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P05\\parts_to_work_on.csv', delimiter = ',', dtype=str)
    # print(parts2.shape)
    # print(parts2.ndim)

    print('<transpose>')
    parts3 = parts2.T
    # (parts3.shape)
    # print(parts3.ndim)
    print(parts3)

except FileNotFoundError: 
    print('File not found.')
except Exception as e:
    print('An error occurred:', e)