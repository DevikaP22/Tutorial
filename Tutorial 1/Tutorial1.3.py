def oddoreven(n):
    if n==0:
        print(f"{n} is zero.")
    elif n%2==0:
        print(f"{n} is even.")
    else:
          print(f"{n} is odd.")

num=int(input("Enter the number: "))
check=oddoreven(num)