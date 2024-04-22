def is_prime(num):
    
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

def generate_primes(n):
    
    primes = []
    num = 2  
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


N = 10
prime_array = generate_primes(N)
print("First", N, "prime numbers:", prime_array)
