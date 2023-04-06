n = 1
for i in range(1000):
    n *= 2

print(sum([int(i) for i in str(n)]))