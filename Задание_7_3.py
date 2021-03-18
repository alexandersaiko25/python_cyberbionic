import math
from functools import reduce
import operator

def simple_number(n):
    if n == 0:
        print("С нулем много не сделаешь")
    elif n == 1:
        print("Единица не считается простым числом")
    elif n // n:
        my_list = []
        for index in range(1,n+1):
            my_list.append(index)
        print(my_list)
        a = input("Если хотите умножить все элементы, нажмите - * , сложить - +, ничего не делать - ok: ")
        if a == "*":
            print(reduce(operator.mul, my_list,1))
        elif a == "+":
            total = sum(my_list)
            print(total)
        elif a == "ok":
            print("OK")
        else:
            print("Заглушка")


simple_number(3)
