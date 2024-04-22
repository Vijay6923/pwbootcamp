arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

arr_transposed = zip(*arr)
col_sums = [sum(col) for col in arr_transposed]
for i, col_sum in enumerate(col_sums):
    print(f"Sum of column {i + 1}: {col_sum}")
