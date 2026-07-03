arr = [1, 2, 3, 4, 5, 6, 5, 8, 4, 4, 4, 3, 3, 5]
f = {}
for x in arr:
    f[x] = f.get(x, 0) + 1
mx = 0
rst = 0
for key in f:
    if f[key] > mx:
        mx = f[key]
        rst = key
print(rst)