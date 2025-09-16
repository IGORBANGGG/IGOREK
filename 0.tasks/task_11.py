a = [10, 3, 5, 7, 9]
min = a[0]
for i in range(1, len(a)):
    if a[i] < min:
        min = a[i]
print(min)