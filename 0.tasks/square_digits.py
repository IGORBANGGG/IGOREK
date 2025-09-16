x = '12345'
s = []
for s1 in x:
    s += s1
square = [int(haha) ** 2 for haha in s]
m = "".join(str(haha) for haha in square)
print(m)
