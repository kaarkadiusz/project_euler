months = {
    0: 31,
    1: 28,
    2: 31,
    3: 30,
    4: 31,
    5: 30,
    6: 31,
    7: 31,
    8: 30,
    9: 31,
    10: 30,
    11: 31,
}
day = 1
counter = 0
for year in range(1901, 2001):
    leap_year = True if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else False
    for month in range(0, 12):
        if day == 6:
            counter += 1
        days = months[month]
        days += 1 if month == 1 and leap_year else 0
        day = (day + days) % 7

print(counter)