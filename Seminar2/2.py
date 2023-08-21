# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

def fibonachi_find(n):
    n1 = 0
    n2 = 1
    res = 0
    counter = 2
    while res < n:
        res = n1 + n2
        n1 = n2
        n2 = res
        counter += 1
    if res == n:
        return counter
    else:
        return (f"Вы ввели число не из ряда фибоначи, ближайшее число {n1}")


n = int(input('Введите число ->'))
print(fibonachi_find(n))
