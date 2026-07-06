import sys

input = sys.stdin.readline

MAX = 1000000

# divisor count
div = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        div[j] += 1

arr = list(range(1, MAX + 1))

arr.sort(key=lambda x: (div[x], -x))

q = int(input())

for _ in range(q):
    n = int(input())
    print(arr[n - 1])