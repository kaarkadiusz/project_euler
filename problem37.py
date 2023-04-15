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

primes = set(["2", "3", "5", "7"])
truncatable_primes = []

iterator = 9
while len(truncatable_primes) < 11:
    iterator += 2
    if not is_prime(iterator):
        continue
    s = str(iterator)
    primes.add(s)
    for i in range(len(s) - 1):
        if s[i+1:] not in primes or s[:-i-1] not in primes:
            break
    else:
        truncatable_primes.append(int(s))

print(truncatable_primes)
print(sum(truncatable_primes))