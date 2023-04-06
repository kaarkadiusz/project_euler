ones = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
tenths = {
    2: "twenty",
    3: "thiry",
    4: "fourty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

bigresult = ""

for n in range(1, 1000): 
    if n not in ones:
        n_hundrets = n // 100
        n_tenths = (n % 100) // 10
        n_ones = n % 10
        result = ""
        if n_hundrets > 0:
            result += ones[n_hundrets] + " hundred "
            if n_tenths > 0 or n_ones > 0:
                result += "and "
        if n_tenths == 1:
            result += ones[10 + n_ones]
        elif n_tenths > 1:
            result += tenths[n_tenths] + " "
        if n_tenths != 1 and n_ones > 0:
            result += ones[n_ones]
    else:
        result = ones[n]
    bigresult += result.replace(" ", "")
    
    print(f"{n}: {result}")

bigresult += "onethousand"
print(bigresult)
print(len(bigresult))