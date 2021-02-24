import math

x = (input("Enter X: "))
x = float(x.replace(',','.'))

if -(math.pi) <= x <= math.pi:
    y = math.cos(3*x)
    print("По условиям первого уравнения: y = ", y)
elif x < -(math.pi) or x > math.pi:
    y = x
    print("По условиям второго уравнения: y = ", y)
