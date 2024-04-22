n=int(input())
a=list(map(int,input().split()))
prefix_array=[]
prefix_array.append(a[0])
for i in range(1,len(a)):
    x=prefix_array[i-1]+a[i]
    prefix_array.append(x)
print(prefix_array)