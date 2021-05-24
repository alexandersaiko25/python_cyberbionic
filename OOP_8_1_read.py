import array

def read_file():
    numbers = []
    with open("my_file.txt", "r") as the_file:
        for line in the_file:
            numbers.append(int(line))
        print(numbers)
        print("Сумма всех элементов из файла = ", sum(numbers))

read_file()