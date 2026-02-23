def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter   # returning as a tuple



length = float(input("Enter length: "))
width = float(input("Enter width: "))


area, perimeter = calc_rectangle(length, width)


print(f"Area: {area}, Perimeter: {perimeter}")
