from math import*

def root(a, b, c):
    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + sqrt(d)) / (2 * a)
        root2 = (-b - sqrt(d)) / (2 * a)
        return f"Two real and distinct roots: {root1:.2f}, {root2:.2f}"
    elif d == 0:
        root = -b / (2 * a)
        return f"One real and repeated root: {root:.2f}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = sqrt(abs(d)) / (2 * a)
        return f"Complex roots: {real_part:.2f} ± {imaginary_part:.2f}i"

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation (a should not be zero).")
else:
    print(root(a, b, c))
