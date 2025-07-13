import numpy as np #
import pandas as pd
#(np)
try: 
    main_path = (['C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P05\\mars_base_main_parts-001.csv', 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P05\\mars_base_main_parts-002.csv', 'C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P05\\mars_base_main_parts-003.csv'])
    main_list = []

    a1 = np.genfromtxt(main_path[0], delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
    a2 = np.genfromtxt(main_path[1], delimiter=',', skip_header=1, dtype=None, encoding='utf-8')
    a3 = np.genfromtxt(main_path[2], delimiter=',', skip_header=1, dtype=None, encoding='utf-8')

    merge_a = np.vstack((a1,a2,a3))

    parts = np.unique(merge_a['f0']) 
    for name in parts: 
        strength_values = merge_a['f1'][merge_a['f0'] == name] #merge values
        # print(f"{name}: {strength_values}")

    print('-'*8, 'FL < 50', '-'*8)

