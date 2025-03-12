
s= input("Enter the string : ")
l1=list(s)
odd=[ ]
even=[]
for i in range(len(l1)):
    if i%2==0:
        even.append(l1[i])
    else:
        odd.append(l1[i])

print(l1)
print("even elements = ",even)
print("odd elements = ",odd)