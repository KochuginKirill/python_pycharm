def sum(a, b):
    if b == 0:
        return a
    return sum(a+1, b-1)



a = 3
b = 5
print(sum(a, b))