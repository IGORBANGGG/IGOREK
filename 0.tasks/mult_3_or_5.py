s = 0
x = int(input())
if x < 0: 
    print("nonono")
for i in range(1, x+1):
    if (i % 3 == 0) or (i % 5 == 0) or (i % 3 == 0 and i % 5 == 0):
        s += i
print(s)
