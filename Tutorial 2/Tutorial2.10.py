
s=input("Enter the passsword ")
Upper=False
Lower=False
hasdig=False
hasspec=False
spcial="$@#"

if(len(s)>=6):
    for i in s:
        if i.islower():
            Lower=True
        elif i.isupper():
              Upper=True
        elif i.isdigit():
              hasdig=True
        elif i in spcial:
            hasspec=True

    if Upper and Lower and hasdig and hasspec:
         print(" Pasword is vlaid")
    else:
         print("Invalid password")

else:
    print("invalid password")                        
