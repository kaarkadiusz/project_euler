def nextCollatzNumber(n):
    return n//2 if n % 2 == 0 else 3*n + 1


dictionary = {
    1: 1
}
counter = 1
list = []
for myNumber in range(2, 10 ** 6 + 1):
    if myNumber in dictionary:
        continue
    i = myNumber
    while i != 1:
        if i in dictionary:
            counter += dictionary[i] - 1
            i = 1
        else:
            i = nextCollatzNumber(i)
            list.append(i)
            counter += 1
    dictionary[myNumber] = counter
    for i in range(len(list)):
        dictionary[list[i]] = counter - i - 1
    counter = 1
    list = []

print(max(dictionary, key=dictionary.get))