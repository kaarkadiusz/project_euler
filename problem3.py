number = 600851475143
k = 2
while number != 1:
    if number%k == 0:
        number /= k
    else: 
        k += 1
print(k)