def sumavg(numbers):
    pos = 0  
    neg = 0  
    posc = 0  
    negc = 0 

    for n in numbers:
        if n > 0:
            pos += n
            posc += 1
        elif n < 0:
            neg += n
            negc += 1

   
    pos_avg = pos / posc if posc > 0 else 0
    neg_avg = neg / negc if negc > 0 else 0

    return pos, pos_avg, neg, neg_avg


nums = []
for i in range(4):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)


pos, pos_avg, neg, neg_avg = sumavg(nums)


print(f"Sum of positive numbers: {pos}")
print(f"Average of positive numbers: {pos_avg:.2f}")
print(f"Sum of negative numbers: {neg}")
print(f"Average of negative numbers: {neg_avg:.2f}")
