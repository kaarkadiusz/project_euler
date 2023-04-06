multiples = [i for i in range(3, 1000, 3)] + [i for i in range(5, 1000, 5)]

for i in range(15, 1000, 15):
    multiples.remove(i)

print(sum(multiples))