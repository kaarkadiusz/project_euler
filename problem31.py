target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0 for _ in range(target)]

for coin in coins:
    for i in range(coin, target+1):
        if coin <= i:
            ways[i] += ways[i-coin]

print(ways[target])