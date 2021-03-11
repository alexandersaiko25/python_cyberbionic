a = input("Введите слово: ")
a = a.casefold()
reverse_a = reversed(a)

if list(a) == list(reverse_a):
    print("Строка палиндром.")
else:
    print("Строка не палиндром")