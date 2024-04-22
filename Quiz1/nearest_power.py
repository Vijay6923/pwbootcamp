import math
number = int(input("Enter a number: "))

if number <= 0:
    print("Invalid input")
else:
    exponent = math.ceil(math.log2(number))
    nearest_power = 2 ** exponent

    print(f"The nearest power of two for {number} is {nearest_power}")
