x = int(input("enter year: "))
x1 = int(input("enter month: "))
if x1 == 1 or x1 == 3 or x1 == 5 or x1 == 7 or x1 == 8 or x1 == 10 or x1 == 12:
    print(31)
if x1 == 4 or x1 == 6 or x1 == 9 or x1 == 11:
    print(30)
if ((x % 4 == 0 and x % 100 != 0) or x % 400 == 0) and x1 == 2:
    print(29)
else: 
    print(28)