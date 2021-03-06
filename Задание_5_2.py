a = -5
def func_1(a):
    while a < 5.1:
        result_1 = a**2
        print(result_1)
        a += 0.5

def func_2(a):
    while a < 5.1:
        result_2 = a**3
        print(result_2)
        a += 0.5
print("Вывод возведения в квадрат!")
func_1(a)
print("Вывод возведения в куб!")
func_2(a)