arr = [3,3,45,45,521,421,324,4254,2132,43,45,521]
f ={}
freq = {}
for x in arr:
    if x in f:
        f[x] += 1
    else:
        f[x] = 1
print(f)


freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1
print(freq)