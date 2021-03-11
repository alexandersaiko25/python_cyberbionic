def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return f(n-1) + f(n-2) + f(n-3)


#f(10)
print(f(12))