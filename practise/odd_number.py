n=int(input("enter the number: "))
a=int(input("enter 1st term: "))
d=int(input("enter the common difference: "))
for i in range(1,n,2): 
    print(i)
for i in range(a,a+(n-1)*d+1,d): 
    print(i)
for i in range(1,21): 
    print(n,"x" ,i,"=",n*i)

