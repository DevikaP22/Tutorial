"""Write a Python program to print n’th Fibonacci number using recursion."""
def FIb(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return FIb(n - 1) + FIb(n - 2)

# Example usage
n = int(input("Enter the position (n) to find the Fibonacci number: "))
print(f"The {n}th Fibonacci number is: {FIb(n)}")
