import problemsmodule as pm

result = "1"
for i in range(1, 101):
    result = pm.StringTimesString(result, str(i))

print(sum([int(i) for i in result]))