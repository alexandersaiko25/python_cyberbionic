def sum(a,b):
    return a + b

def subtraction(a,b):
    return  a - b

def mult(a,b):
    return a * b

def division(a,b):
    if b == 0:
        print("Ошибка! На ноль делить нельзя")
    else:
        return a/b

def calc():

    while True:
        action = input("Введите опрерацию(+|-|*|/): ")
        a = int(input("Введите первое число: "))
        b = int(input("Введите второе число: "))

        if action == "+":
            print(sum(a,b))
        elif action == "-":
            print(subtraction(a,b))
        elif action == "*":
            print(mult(a,b))
        elif action == "/":
            print(division(a, b))
        else:
            print("Что-то пошло не так")

        repeat = input("Хотите повторить?")
        if repeat != "y":
            return
calc()




