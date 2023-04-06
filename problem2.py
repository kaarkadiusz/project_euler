sequence = []
prevterm = 0
currterm = 1
while currterm < 4*10**6:
    tmp = currterm
    currterm = prevterm + currterm
    prevterm = tmp
    if currterm%2 == 0:
        sequence.append(currterm)
print(sum(sequence))