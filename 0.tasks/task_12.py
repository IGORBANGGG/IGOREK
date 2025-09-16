x = int(input("enter number: "))
x1 = input("bytes or kilobytes? ")
if x1 == "bytes":
    print(x)
if x1 == "kilobytes":
    print(x//1024)