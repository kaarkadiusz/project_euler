products = []
for i in range(10, 99):
    t1, t2 = i // 10, i % 10
    if t1 == t2 or t2 == 0:
        continue
    for j in range(100, 999):
        mySet = {t1, t2}
        t3, t4, t5 = j // 100, (j//10) % 10, j % 10
        mySet.update([t3, t4, t5])
        if len(mySet) != 5 or t4 == 0 or t5 == 0:
            continue
        product = i * j
        if product // 10000 != 0:
            break
        t6, t7, t8, t9 = product % 10, (product // 10) % 10, (product // 100) % 10, product // 1000
        mySet.update([t6, t7, t8, t9])
        if len(mySet) != 9 or 0 in mySet:
            continue
        else:
            products.append(product)
for i in range(1, 10):
    t1 = i
    for j in range(1000, 9999):
        mySet = {t1}
        t2, t3, t4, t5 = j % 10, (j // 10) % 10, (j // 100) % 10, j // 1000
        mySet.update([t2, t3, t4, t5])
        product = i * j
        if product // 10000 != 0:
            break
        t6, t7, t8, t9 = product % 10, (product // 10) % 10, (product // 100) % 10, product // 1000
        mySet.update([t6, t7, t8, t9])
        if 0 in mySet:
            continue
        if len(mySet) != 9:
            continue
        else:
            products.append(product)

products = list(set(products))
products.sort()
print(products)
print(sum(products))