from math import pi
def calculate_cirle_area():
    radius = float(input("the radius of the circle : "))
    area = pi * (radius ** 2)
    print(f"The are of the circle with radius {radius} is {area:.16f} ")

calculate_cirle_area()

def get_file_extension():
    filename = input("Input the Filename: ")    
    file_extension = filename.split('.')[-1]
    extension_map = {'py': 'python'}
    extension_description = extension_map.get(file_extension, file_extension)
    print(f"The extension of the file is : '{extension_description}'")

get_file_extension()