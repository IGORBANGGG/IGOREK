a = [1, 2, 3, 4, 4, 4, 5, 5, 6, 7]
b = [1, 4, 5]
result = []
for vse in a:
    if vse not in b:
        result.append(vse)
print(result)
