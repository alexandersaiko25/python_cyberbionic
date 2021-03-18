def f(n):
    count = 0
    a,b = 0,1
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    my_list = []
    while count < n:
        total = a + b
        a = b
        b = total
        my_list.append(a)
        count += 1
    print(my_list)


#f(10)
print(f(13))