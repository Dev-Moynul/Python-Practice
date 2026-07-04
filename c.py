
n = int(input())

k = 0
s = 0

while s + (k + 1) <= n:
    k += 1
    s += k

arr = []

for i in range(1, k):
    arr.append(i)
    

arr.append(k + (n - s))
arr.reverse()

print(k)
print(*arr)