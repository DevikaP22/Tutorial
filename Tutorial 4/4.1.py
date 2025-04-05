class Arith:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def read(self):
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero is not allowed"

    def display(self):
        print(f"First number: {self.num1}")
        print(f"Second number: {self.num2}")

def main():
    arith = Arith()
    while True:
        print("\nArithmetic Operations Menu:")
        print("1. Read numbers")
        print("2. Add")
        print("3. Subtract")
        print("4. Multiply")
        print("5. Divide")
        print("6. Display numbers")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            arith.read()
        elif choice == 2:
            print(f"Sum: {arith.add()}")
        elif choice == 3:
            print(f"Difference: {arith.sub()}")
        elif choice == 4:
            print(f"Product: {arith.mul()}")
        elif choice == 5:
            print(f"Quotient: {arith.div()}")
        elif choice == 6:
            arith.display()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
