x = int(input("Distance in meters: "))
x2 = int(input("Distance in kilometers: "))
x3 = x2*1000
if x3<x:
    print(x3)
if x<x3:
    print(x)
if x == x3:
    print("numbers are the same")