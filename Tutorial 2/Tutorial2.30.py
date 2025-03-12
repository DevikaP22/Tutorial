

def remvDup(lst):
    l = []
    for item in lst:
        if item not in l:
            l.append(item)
    return l

n = int(input("Enter the number of elements: "))
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(n)]

print(f"\nList after removing duplicates: {remvDup(numbers)}")
