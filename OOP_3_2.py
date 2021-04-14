class Calc:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        print(self.x + self.y)

    def substraction(self):
        print(self.x - self.y)

    def multiplication(self):
        print(self.x * self.y)

    def division(self):
        try:
            print(self.x / self.y)
        except ZeroDivisionError as e:
            print(e)


    def exponentiation(self):
        try:
            print(self.x ** self.y)
        except ZeroDivisionError as e:
            print(e)

"""Программа-Калькулятор"""
x = int(input("Введите значение Х: "))
y = int(input("Введите значение Y: "))
total = Calc(x, y)

action = input("Введите действие, которое нужно сделать |+|-|*|/|**| : ")
if action == "+":
    total.addition()
elif action == "-":
    total.substraction()
elif action == "*":
    total.multiplication()
elif action == "/":
    total.division()
elif action == "**":
    total.exponentiation()

