import pandas as pd

# Mars_Base_Inventory_List.csv
try:
    with open("C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P03\\Mars_Base_Inventory_List.csv", 'r', encoding = 'utf-8') as file1:
        for line in file1:
            print(line.strip())
# Flammability_descending
        print('----- 정렬(Flammability : 내림차순) -----')

        arr = []

    with open("C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P03\\Mars_Base_Inventory_List.csv", 'r', encoding = 'utf-8') as file1:
        next(file1)
        file2 = file1.readlines()
        for line in file2:
            Substance,Weight_g_per_cm3,Specific_Gravity,Strength,Flammability = line.split(',')
            arr.append([Substance,Weight_g_per_cm3,Specific_Gravity,Strength,Flammability.strip()])
            sorted_arr = sorted(arr, key=lambda x: x[4], reverse=True)
    for i in arr:
        print(i)


    print('----- 구분 -----')


# Flammability>=0.7_List
    print('----- 목록지정_Flammability>=0.7 -----')
    filtered_list = [x for x in sorted_arr if float(x[4])>=0.7]
    for item in filtered_list:
        print(item)

#Create csv
    df = pd.DataFrame(filtered_list, columns=["Substance", "Weight_g_per_cm3", "Specific_Gravity", "Strength", "Flammability"])
    df.to_csv('Mars_Base_Inventory_danger.csv', index=False)
#Create binary
    df.to_pickle('Mars_Base_Inventory_List.bin')
    df2 = pd.read_pickle('Mars_Base_Inventory_List.bin')
    print(df2)

except FileNotFoundError:
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)