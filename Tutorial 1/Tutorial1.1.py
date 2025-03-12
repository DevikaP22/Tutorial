def dateformat(s):
        h=s//3600
        m=(s%3600)//60
        s=s%60
        return f"{h:02}:{m:02}:{s:02}"

s=int(input("Enter the time in seconds: "))
time=dateformat(s)
print("Time in HH:MM:SS format",time)