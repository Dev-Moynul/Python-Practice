from collections import Counter
arr = [3, 4, 5, 3, 4, 6, 6, 5 ,9]
c = Counter(arr)
print(c)
print(c[5])
print(c[100])