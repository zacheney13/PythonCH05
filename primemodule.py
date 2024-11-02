def is_prime(n):
    if n <= 1: 
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    for i in range(2, n):
        if is_prime(i):
            print(i)
            
def get_primes(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    print(primes)