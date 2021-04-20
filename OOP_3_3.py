
while True:
    try:
        name_input = input("Введите имя сотрудника: ")
        surname_input = input("Введите фамилию сотрудника: ")
        department_input = input("Введите отдел сотрудника: ")
        year_input = int(input("Введите год поступления на работу: "))
    except(ValueError,TypeError, UnboundLocalError) as error:
        print("Вы ввели некорректные данные:", error)
        print("Повторите ввод!")

    if year_input >= 2005:
        print(("Данные сотрудника принятого на работу с 2005: ", name_input, surname_input, department_input, year_input))
    else:
        continue
