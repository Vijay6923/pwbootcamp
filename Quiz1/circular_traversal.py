def circular_traversal(array, start_index):

    n = len(array)
    traversal = []
    current_index = start_index % n 

    for _ in range(n):
        traversal.append(array[current_index])
        current_index = (current_index + 1) % n  

    return traversal

n=int(input())
arr = list(map(int,input().split()))
start_index = 2
result = circular_traversal(arr, start_index)
print("Circular traversal starting from index", start_index, ":", result)
