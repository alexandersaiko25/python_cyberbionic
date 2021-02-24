import math
operation = input("Введите одну из необходимых операций(+,-,*,/,**2,sin,cos,tan): ")

if operation == "+":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    total = a + b
    print(total)
elif operation == "-":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    total = a - b
    print(total)
elif operation == "*":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    total = a * b
    print(total)
elif operation == "/":
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    total = a / b
    print(total)
elif operation == "**2":
    a = int(input("Введите число: "))
    total = a**2
    print(total)
elif operation == "cos":
    a = int(input("Введите число: "))
    total = math.cos(a)
    print(total)
elif operation == "sin":
    a = int(input("Введите число: "))
    total = math.sin(a)
    print(total)
elif operation == "tan":
    a = int(input("Введите число: "))
    total = math.tan(a)
    print(total)
else:
    print("Вы не ввели математическую операцию!")

