string = input("Enter string: ")
shift = int(input("Enter the number of positions to left shift: "))
k = shift % len(string)
final_string = string[k:] + string[:k]
print("Left shifted string:", final_string)
