class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

def main():
    
    num1 = Complex(3, 4)
    num2 = Complex(1, 7)

    
    result = num1 + num2

    
    print(f"Complex Number 1: {num1}")
    print(f"Complex Number 2: {num2}")
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
