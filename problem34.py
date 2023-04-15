def Factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * Factorial(n - 1)

factorials = {str(i): Factorial(i) for i in range(0, 10)}
digit_factorials = []

for i in range(3, 100000):
    digits = [k for k in str(i)]
    if i == sum([factorials[k] for k in digits]):
        digit_factorials.append(i)

print(sum(digit_factorials))