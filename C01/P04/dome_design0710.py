import math

#전역변수 
material = None
diameter = None
thickness = None
area = None
weight = None

def check_quit(value: str):
    if value == 'q':
        print("프로그램 종료.")
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
    material = 'glass'
    density_earth = 2.4
    thickness = 1
    print('< q 입력 시, 프로그램이 종료됩니다. >')
    input_material = input('재질을 입력하세요. [기본 값 : glass] ').strip()
    check_quit(input_material)
    if (input_material):
        material = input_material
    if material == 'glass':
        density_earth = 2.4 #g/cm³
    elif material == 'aluminum':
        density_earth = 2.7
    elif material == 'carbon_steel':
        density_earth = 7.85
    else:
        print('Unknown material. Retry.') 
        continue

    diameter = input('구의 지름을 입력하세요.(m) : ')
    check_quit(diameter)
    diameter = float(diameter)
    if diameter == 0:
        print('diameter != 0. Retry.') 
        continue

    input_thickness = input('두께를 입력하세요. (cm) [기본 값 : 1cm] ').strip()
    check_quit(input_thickness)
    if(input_thickness):
        thickness = input_thickness
    try:
        thickness = float(thickness)
    except ValueError:
        print("Enter the number.")
    # exit()


    thickness_m = thickness/100
    inner_volume = hemisphere_volume(diameter - 2 * thickness_m)
    shell_volume = hemisphere_volume(diameter) - inner_volume

    mass_earth = density_earth * shell_volume * 1000  #m → cm, g → kg

# Mars_G 3.71
# 9.81/3.71 = 0.38 = G-ratio
    weight_mars = mass_earth * 0.38 
    weight = weight_mars 

    i = sphere_area(diameter, material, thickness)
    area = round((i),3) #m²

    #diameter : m / thickness : cm / area : m² / weight : kg
    print('material =⇒', material, ', diameter =⇒', round(diameter, 3), ', thickness =⇒', round(thickness, 3), ', area =⇒', round(area, 3), ', weight=⇒', round(weight, 3), 'kg')

    answer = input('Do you want to continue?(Y/N): ').strip().upper()
    if answer == 'N':
        print('Exiting program.')
        break