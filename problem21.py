def CalcSumOfDivisors(n: int) -> int:
    suma = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            suma += n // i
    return suma + 1

sums = {}

for i in range(1, 10001):
    sums[i] = CalcSumOfDivisors(i)

suma = 0
for i in sums:
    if sums[i] > 10000: 
        continue
    if i == sums[sums[i]] and i != sums[i]:
        suma += i
        print(f"{i}: {sums[i]}")

print(suma)