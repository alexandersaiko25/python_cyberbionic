a = int(input("Введите число для a: "))
b = int(input("Введите число для b: "))
c = int(input("Введите число для c: "))

d = b ** 2 - 4 * a * c
print(d)
if d < 0:
    print("Под корнем отрицательное чило - ошибка")
elif d == 0:
    x = (-b + d ** 0.5) / 2 * a
    print("Одно решение(т.к. под корнем 0):", x)
else:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print("Первое решение:", x1, sep="")
    print("Второе решение:", x2, sep="")