
def Median(num):
    num.sort()  
    n = len(num)
    
    if n % 2 == 1:
        return num[n // 2]  
    else:
        mid1, mid2 = num[n // 2 - 1], num[n // 2]  
        return (mid1 + mid2) / 2  

n = int(input("Enter the number of elements: "))


numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: ")) 
    numbers.append(num)


median = Median(numbers)
print(f"\nThe median is: {median}")
