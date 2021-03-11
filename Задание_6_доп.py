def func_recursion(n):
    if n == 1:
        return 1
    return n + func_recursion(n-1)

print(func_recursion(4))
