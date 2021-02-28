h = int(input(" Введите ширину прямоугольника: ")) + 1
w = int(input(" Введите длину прямоугольника: ")) + 1
i = 1
j = 1
while i < h:
    j = 1
    while j < w:
        print("*",end="")
        j = j + 1
    print()
    i = i + 1


