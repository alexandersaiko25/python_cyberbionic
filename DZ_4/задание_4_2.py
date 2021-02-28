n = int(input("Введите число для вычисления факториала: "))
a = 1
for i in range(1,n,1):
    i += 1
    a = i * a
print(a)