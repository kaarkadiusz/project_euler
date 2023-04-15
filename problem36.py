s = "585"

numbers = []

for i in range(10**6):
    s = str(i)
    if bin(i)[2:] == bin(i)[2:][::-1] and s == s[::-1]:
        numbers.append(i)

print(numbers)
print(sum(numbers))