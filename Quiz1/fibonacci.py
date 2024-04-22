def is_fibonacci(arr):
    if len(arr) < 3:
        return False
    
    for i in range(2, len(arr)):
        if arr[i-2] + arr[i-1] != arr[i]:
            return False
    
    return True
n=int(input())
sequence = list(map(int,input().split()))
print(is_fibonacci(sequence)) 

non_sequence = [1, 2, 4, 7, 11]
print(is_fibonacci(non_sequence)) 
