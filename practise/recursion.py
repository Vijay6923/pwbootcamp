def sum_of_digits(n):
    if n < 10:
        return n
    else:
    
        last_digit = n % 10
        
        return last_digit + sum_of_digits(n // 10)


n=int(input())
print(sum_of_digits(n))
