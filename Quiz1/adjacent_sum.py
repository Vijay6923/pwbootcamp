n=int(input())
array = list(map(int,input().split()))
sums = []
for i in range(len(array) - 1):
    adjacent_sum = array[i] + array[i + 1]
    sums.append(adjacent_sum)
print("Sums of adjacent values:", sums)
