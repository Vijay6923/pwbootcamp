n=int(input("Enter the number: "))
num=2
prime=0
while(prime<n):
    is_prime=True
    i=2
while(i<num):
    if(num%i==0):
        is_prime=False
        break
    i=i+1
    if(is_prime==True):
        print(num)
        prime=prime+1
        num=num+1
    
