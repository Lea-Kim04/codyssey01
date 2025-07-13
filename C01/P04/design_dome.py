import math

#전역변수 
material = None
diameter = None
thickness = None
area = None
weight = None

def check_quit(value: str):
    if value == 'q':
        print('프로그램 종료.')
        exit()

def sphere_area(diameter, material, thickness):
    _ = material
    _ = thickness
    radius = diameter / 2
    result_sphere_area = 4 * math.pi * radius**2 
    result_hemisphere_area = result_sphere_area / 2
    return result_hemisphere_area #m²

def hemisphere_volume(diameter):
    radius = diameter / 2
    result_hemisphere_volume = (2/3) * math.pi * (radius ** 3) 
    return result_hemisphere_volume #m³

while True:
    material = '유리'
    density_earth = 2.4
    thickness = 1
    print('< q 입력 시, 프로그램이 종료됩니다. >')
    input_material = input('재질을 입력하세요. [기본 값 : 유리] ').strip()
    check_quit(input_material)
    if (input_material):
        material = input_material
    if material == '유리':
        density_earth = 2.4 #g/cm³
    elif material == '알루미늄':
        density_earth = 2.7
    elif material == '탄소강':
        density_earth = 7.85
    else:
        print('알 수 없는 재질입니다. 재입력하세요.') #raise 예외처리 안함. #재질
        continue

    diameter = input('구의 지름을 입력하세요.(m) : ') #지름
    check_quit(diameter)
    diameter = float(diameter)
    if diameter == 0:
        print('지름은 0이 될 수 없습니다. 재입력하세요.') #raise 예외처리 안함.
        continue

    input_thickness = input('두께를 입력하세요. (cm) [기본 값 : 1cm] ').strip()
    check_quit(input_thickness)
    if(input_thickness):
        thickness = input_thickness
    # 위 로직대로 진행하면 thickness에 1이 할당된 뒤 input으로 들어오는 값이 입력됨.
    # 원하는 로직은 입력된 값이 없으면 기본 값 1 이 입력되어야 함.
    # 그러면 입력 받은 값을 검증 후 1 이나 입력값을 사용.
    try:
        thickness = float(thickness)
    except ValueError:
        print('숫자를 입력해야 합니다.')
    # exit()


    thickness_m = thickness/100
    inner_volume = hemisphere_volume(diameter - 2 * thickness_m)
    shell_volume = hemisphere_volume(diameter) - inner_volume

    mass_earth = density_earth * shell_volume * 1000  #m → cm, g → kg

    weight_mars = mass_earth * 0.38 
    weight = weight_mars #무게

    i = sphere_area(diameter, material, thickness)
    area = round((i),3) #m² #면적

    #지름 : m / 두께 : cm / 면적 : m² / 무게 : kg
    print('재질 =⇒', material, ', 지름 =⇒', round(diameter, 3), ', 두께 =⇒', round(thickness, 3), ', 면적 =⇒', round(area, 3), ', 무게 =⇒', round(weight, 3), 'kg')

    answer = input('계속하시겠습니까? (Y/N): ').strip().upper()
    if answer == 'N':
        print('프로그램 종료.')
        break


