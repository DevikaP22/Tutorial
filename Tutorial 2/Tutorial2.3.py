
def isPal(s):
    n=len(s)
    left=0
    for i in range(0, int(n/2)):
       if s[i] != s[n-i-1]:
           return False
    return True


s= input("Enter the string : ")
if isPal(s):
    print(" is paliendrome")
else :
    print("is not palidrome")