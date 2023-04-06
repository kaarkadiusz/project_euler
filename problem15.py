# TODO jak będzie mi się kiedyś chciało to zrobić pisemne mnożenie (metode StringTimesString)
n = 1
k = 0
for i in range(1, 41):
    n = n * i
    if i == 20:
        k = n

print(f"{n // (k*k)}")