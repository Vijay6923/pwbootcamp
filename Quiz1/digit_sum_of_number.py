n=int(input())
sum=0
while(n!=0):
    r=n%10
    sum+=r
    n=n//10
print(sum)
