import math

def prime(x):

    if x == 1:
        print("Единица не считается простым числом")
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

my_list = []
j = int(input("Какое самое большое число в списке? : "))
for number in range(2, j):
    if prime(number):
        my_list.append(number)
print(my_list)
a = input("Если хотите умножить все элементы, нажмите - * , сложить - +, ничего не делать - ok: ")
if a == "*":
    print(math.prod(my_list))
elif a == "+":
    print(sum(my_list))
else:
    pass

