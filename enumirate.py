# symple process
arr = [10, 5, 30]
for i in range(len(arr)):
    print(i, arr[i])


#Enumirate
arr = [10, 5, 30]
for i, x in enumerate(arr):
    print(i, x)

#Starting Index Change
arr = [10, 5, 30]
for i, x in enumerate(arr, start=1):
    print(i, x)

#Ami jante cai 9 kon index er moddhe ache
arr = [5,7,9,2]
for i, x in enumerate(arr):
    if x == 9:
        print(i)

#Arr update korte cai
arr = [5,7,9,2]
for i, x in enumerate(arr):
    arr[i] = x * 2
print(arr)