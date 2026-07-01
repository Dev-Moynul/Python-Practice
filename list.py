input
arr = list(map(int,input().split()))
print (len(arr))
for x in arr:
    print(arr)

for i  in range(len(arr)):
    print(arr[i])

arrr = [5, 6, 6 ,3, 14, 75]
print(arrr, arrr.sort(reverse=True))

print(max(arrr))

arrr[::-1]
print(arrr)
print(arrr,arrr.index(6))


arr = [4,5,6,7,8,9,10]
#arr.insert(4,100)
arr.pop(2)
print(arr)
print(arr[:])
print(arr[::-1])
arr.sort()
print(arr)