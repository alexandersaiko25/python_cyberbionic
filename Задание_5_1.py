def hello(name):
    if name == "":
        print("Hello, Alexander")
    else:
        print("Hello, " + name)

name = input("Введите Ваше имя: ")
hello(name)