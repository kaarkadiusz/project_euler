from collections import Counter
results = []
for a in range(1, 500):
    for b in range(a + 1, 500):
        c = (a**2 + b**2)**0.5
        if c.is_integer() and (a + b + c) <= 1000:
            results.append(a+b+c)

print(Counter(results).most_common(1))