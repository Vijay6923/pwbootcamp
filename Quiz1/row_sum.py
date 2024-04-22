arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
row_sums = [sum(row) for row in arr]
for i, row_sum in enumerate(row_sums):
    print(f"Sum of row {i + 1}: {row_sum}")
