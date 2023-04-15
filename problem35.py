def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    limit = int(n**0.5)
    for i in range(5, limit+1, 6):
        if n % i == 0 or n % (i+2) == 0:
            return False
    return True

def shift_string(s: str) -> str:
    return s[-1:] + s[:-1]
    

primes = {"2", "3"}
for i in range(5, 10**6, 2):
    if is_prime(i):
        primes.add(str(i))

circular_primes = set()
for prime in primes:
    # if prime in circular_primes:
    #     continue
    s = prime
    for i in range(len(s) - 1):
        s = shift_string(s)
        if s not in primes:
            break
    else:
        circular_primes.add(prime)
        s = prime
        for i in range(len(s) - 1):
            s = shift_string(s)
            if s in circular_primes:
                continue
            circular_primes.add(s)

print(circular_primes)
print(len(circular_primes))