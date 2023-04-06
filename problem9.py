suma = 0
m = 2
while suma != 1000:
    for n in range(1, m + 1):  
        a = m * m - n * n
        b = 2 * m * n
        c = m * m + n * n
        if a+b+c == 1000:
            suma = 1000
            print(f"{a}, {b}, {c}: {a**2} + {b**2} = {c**2} => {a} * {b} * {c} = {a*b*c}")
    m += 1