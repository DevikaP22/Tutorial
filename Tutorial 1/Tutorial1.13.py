def reverse(n):
    reversed = 0
    
    while n > 0:
        digit = n % 10 
        reversed = reversed * 10 + digit  
        n //= 10
    
    return reversed

num = int(input("Enter a number: "))

if num < 0:
    print(f"Reversed number: -{reverse(abs(num))}")
else:
    print(f"Reversed number: {reverse(num)}")
