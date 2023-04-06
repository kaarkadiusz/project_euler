number = 2520
notFound = True
while notFound:
    number += 2520
    for i in range(11, 21):
        if number%i != 0:
            break
        if i == 20:
            notFound = False
print(number)