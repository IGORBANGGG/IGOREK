def f(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)
s = 0
for n in range(1, 34):
    if f(n) % 2 == 0:
        s += f(n)
print(s)





