a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=int(input("Enter 3rd Number: "))
if(a>b):
    if (a>c):
        largest=a
    else:
        largest=c
else:
    if(b>c):
        largest=b
    else:
        largest=c

print("largest number: ",largest)
