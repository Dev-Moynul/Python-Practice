arr = [5, 2, 5, 1, 2, 5, 7, 7]
f = {}
for x in arr:
    f[x] = f.get(x, 0) + 1
for key, value in f.items():
    print(key, value)