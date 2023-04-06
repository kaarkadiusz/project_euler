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

primes = [3]
for i in range(-999, 1001, 2):
    if is_prime(i):
        primes.append(i)

bestPrimesCount = 0
bestAandB = (0, 0)

for b in primes:
    for a in range(-999, 1000, 2):
        n = 1
        count = 1
        # print(a, b)
        while True:
            # print(count, end=" ")
            if is_prime(n**2 + a*n + b):
                count += 1
                n += 1
            elif count > bestPrimesCount:
                bestPrimesCount = count
                bestAandB = (a, b)
                break
            else:
                break
                
print(bestPrimesCount)
print(bestAandB)