n=int(input("enter the value of n: "))
a=int(input("enter the first term: "))
r=int(input("enter the common ratio: "))
for i in range(a,a*(r**n-1),r):
    print(i*r)