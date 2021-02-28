size = 10
row = 1

while row <= size:
    column = 1
    while column <= row:
        print("*",end="")
        column += 1
    print()
    row += 1
print("", end="")

