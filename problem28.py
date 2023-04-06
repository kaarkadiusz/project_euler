counter = 1
increment = 2

numbers = [counter]

i = 0
while(i * 2 + 1 <= 1001):
    print(f"{i*2+1}x{i*2+1}\t{sum(numbers)}")
    for j in range(4):
        numbers.append(numbers[-1] + increment)
    increment += 2
    i += 1