list_1 = [1,2,3,-1,4,5,8,9,2]
#list_2 = [3,4,5,8,7,3,1,4]

def action_for_list(list):
    total = 0
    for index in list_1:
        total = total + index

        average = total / len(list_1)

    print("Сумма всех значений в списке =", total)
    print("Среднее арифметическое всех значений в списке =", round(average,2))
    print("Максимальное значение в списке =", max(list_1))
    print("Минимальное значение в списке =", min(list_1))

action_for_list(list_1)
