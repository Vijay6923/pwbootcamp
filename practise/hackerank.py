def superDigit(n, k):

    def calc_super_digit(num):
        if len(num) == 1:
            return int(num)
        
        else:
            digit_sum = sum(int(digit) for digit in num)
            return calc_super_digit(str(digit_sum))
    
    
    initial_super_digit = calc_super_digit(n)
    
    
    super_digit_of_concatenated = calc_super_digit(str(initial_super_digit * k))
    
    return super_digit_of_concatenated


n, k = input().split()
result = superDigit(n, int(k))
print("Super digit:", result)
