a=int(input("Enter 1st side: "))
b=int(input("Enter 2nd side: "))
c=int(input("Enter 3rd side: "))
if(a+b>c)or (a+c>b)or(b+c>a):
    print("triangle is possible")
else:
    print("triangle is not possible")