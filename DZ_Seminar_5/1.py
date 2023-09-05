def f(a, b):
    n = a
    if b == 1:
        return a
    return f(a, b-1) * n


a = 3
b = 5
print(f(a, b))