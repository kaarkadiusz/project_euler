concatenated_products = []
for i in range(1, 10001):
    k = 1
    concatenated_product = ""
    while len(concatenated_product) < 9:
        concatenated_product += str(k*i)
        k += 1
    distinct_digits = set(concatenated_product)
    if len(distinct_digits) == 9 and '0' not in distinct_digits and len(concatenated_product) == 9:
        concatenated_products.append(concatenated_product)

print(max(concatenated_products))