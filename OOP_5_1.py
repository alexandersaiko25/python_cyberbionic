def mean_num(*args):
    total = 0
    for item in args:
        total += item
    print(f"Сумма всех элементов: {total}")
    average = total / len(args)
    print(f"Среднее арифметическое элементов: {average}")
    diapazon = sum(args[3:]) / len(args[3:])
    print(f"Среднее арифметическое в диапазоне с 4го элемента: {diapazon}")
    
mean_num(1, 2, 3, 4, 5)
