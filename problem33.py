results = []
for i in range(10, 100):
    a1, a2 = i % 10, i // 10
    if a1 == 0:
        continue
    for j in range(i+1, 100):
        b1, b2 = j % 10, j // 10
        if b1 == 0:
            continue
        if a1 == b1:
            if i / j == a2 / b2:
                results.append((i, j))
                continue
        elif a1 == b2:
            if i / j == a2 / b1:
                results.append((i, j))
                continue
        elif a2 == b1:
            if i / j == a1 / b2:
                results.append((i, j))
                continue
        elif a2 == b2:
            if i / j == a1 / b1:
                results.append((i, j))
                continue

product = 1
for val in results:
    product *= (val[0] / val[1])

denominator = 0
while True:
    if product * denominator >= 1:
        break
    denominator += 1

print(denominator)