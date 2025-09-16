v1 = int(input("v1: "))
g = int(input("g: "))
v2 = int(input("v2: "))
if v1 >= v2:
    print("чурупаха не догонит")
vdogon = v2 - v1
t = g//vdogon
s = t
if s >= 60 and s < 3600:
    m = t//60
    if m >= 60:
        h = m/60
print(h, m, s)



