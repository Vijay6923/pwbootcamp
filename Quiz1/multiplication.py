def multiplication_table(n):
    table = [[0] * n for _ in range(n)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            table[i-1][j-1] = i * j

    return table
def print_multiplication_table(table):

    for row in table:
        print(" ".join(str(num).rjust(len(str(table[-1][-1]))) for num in row))
limit = 10
table = multiplication_table(limit)
print_multiplication_table(table)
