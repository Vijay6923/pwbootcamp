n=int(input("Enter the number: "))
count=0
i=2
while(i<n):
    if(n%i==0):
        count=count+1
    i=i+1
if count==0:
    output="prime"
else:
    output="not prime"
print(output)