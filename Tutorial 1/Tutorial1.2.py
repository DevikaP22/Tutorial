from math import*

def areaPerimeter(r):
    area=pi*r**2
    perimeter=2*pi*r
    return f"area is: {area:.2f} & perimeter is: {perimeter:.2f}"

r=int(input("Enter the radius of the circle: "))
calc=areaPerimeter(r)
print(calc)