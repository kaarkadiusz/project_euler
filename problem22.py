import urllib.request # the lib that handles the url stuff

data = urllib.request.urlopen("https://projecteuler.net/project/resources/p022_names.txt")
names = data.read().decode('UTF-8').replace("\"", "").split(',')
names.sort()
suma = 0
for index, name in enumerate(names):
    s = sum([ord(c) - 64 for c in name])
    suma += (index + 1) * s
    print(f"{index}: {name} = {s}")

print(suma)