import pandas as pd

# Mars_Base_Inventory_List.csv
try:
    with open("C:\\Users\\jin_y\\Downloads\\codyssey\\C01\\P03\\Mars_Base_Inventory_List.csv", 'r', encoding = 'utf-8') as file1:
        for line in file1:
            print(line.strip())
# Flammability_descending  
        print('----- 정렬_Flammability : 내림차순 -----')

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
    print('----- List_Flammability>=0.7 -----')
    filtered_list = [x for x in sorted_arr if float(x[4])>=0.7]
    for item in filtered_list:
        print(item)

#Create csv
    df = pd.DataFrame(filtered_list, columns=["Substance", "Weight_g_per_cm3", "Specific_Gravity", "Strength", "Flammability"])
    df.to_csv('Mars_Base_Inventory_danger.csv', index=False)

    print ('-------구분(바이너리 출력)-------')
#Create binary
    df.to_pickle('Mars_Base_Inventory_List.bin')
    df2 = pd.read_pickle('Mars_Base_Inventory_List.bin')
    print(df2)


except FileNotFoundError:
    print('파일이 존재하지 않음.')
except Exception as e:
    print('파일 처리 중 오류가 발생.', e)






#텍스트 파일과 바이너리 파일의 차이점
#텍스트 파일 (Text File):
#저장 방식: 문자 기반으로 데이터를 저장
#각 문자는 아스키 코드 또는 유니코드(문자 인코딩)을 사용하여 표현
#가독성: 사람이 쉽게 읽고 이해할 수 있음
#저장 내용: 주로 텍스트, 소스 코드, 설정 파일 등에 사용 
#데이터 표현: 줄 단위로 구분, 각 줄은 특정 의미를 가질 수 있음 
#ex) .txt, .csv, .html 파일 등

#이진 파일 (Binary File):
#저장 방식: 0과 1의 비트 단위로 데이터를 저장 
#가독성: 사람이 읽기에 부적합, 컴퓨터 프로그램이 해석해야 
#저장 내용: 다양한 형태(그림, 오디오, 비디오, 실행 파일, 압축 파일)의 데이터를 저장
#데이터 표현: 데이터의 종류에 따라 다양한 형식으로 저장, 줄 단위로 구분되지 않습니다. 
#ex) .jpg, .mp3, .exe, .zip 파일 등