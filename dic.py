student = {
    "name": "Moynul",
    "age": 20,
    "cgpa": 3.95
}

# value access
print(student["name"])

# value add
student["dept"] = "CSE"
print(student)

#value Update

student["age"] = 21
print(student)

arr = [3, 1, 3, 2, 1, 3, 2]
f ={}
for x in arr:
    f[x] = f.get(x, 0) + 1
print(f)
