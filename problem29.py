numbers = []

for a in range(2, 101):
    for b in range(2, 101):
        numbers.append(a ** b)

numbers = list(set(numbers))

print(len(numbers))