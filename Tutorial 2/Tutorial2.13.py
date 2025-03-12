

import math

def Area(radius):
    if radius < 0:
        return "Radius cannot be negative"
    
    area = math.pi * radius ** 2
    return area


r = float(input("Enter the radius of the circle: "))


print(f"Area of the circle: {Area(r):.2f}")
