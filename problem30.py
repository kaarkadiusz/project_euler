numbers = []
for i in range(11, 1000001):
    n = i
    suma = 0
    while n != 0:
        suma += ((n % 10) ** 5)
        n //= 10
    if suma == i:
        numbers.append(i)

for i in numbers: 
    print(i)

print(sum(numbers))