
s = input().upper()
unique_bowels = set()
for char in s:
    if char == 'A' or char == 'H' or char == 'I' or char == 'M' or char == 'O' or char == 'T' or char == 'U' or char == 'V' or char == 'W' or char == 'X' or char == 'Y':
        unique_bowels.add(char)

print(len(unique_bowels))
