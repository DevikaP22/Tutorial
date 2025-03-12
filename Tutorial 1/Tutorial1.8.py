def SOD(n):
    n = abs(n)
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10

    return total

num = int(input("Enter a number: "))

print(f"Sum of digits: {SOD(num)}")
