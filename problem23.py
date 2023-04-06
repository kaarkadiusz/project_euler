def CalcSumOfDivisors(n: int) -> int:
    suma = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            suma += (n // i) if n // i != i else 0
    return suma + 1

abundnant_numbers = []

limit = 28124

for i in range(1, limit):
    if(CalcSumOfDivisors(i) > i):
        abundnant_numbers.append(i)

sums = []

for i in range(len(abundnant_numbers)):
    for val in abundnant_numbers[i:]:
        if val + abundnant_numbers[i] < limit:
            sums.append(val + abundnant_numbers[i])
        else:
            break

sums = list(set(sums))
sums.sort()
non_sums = [k for k in range(1, limit) if k not in sums]

print(sum(non_sums))
