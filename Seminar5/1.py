# Задача №31. Общее обсуждение
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


def fibonacci_get(n):
    if n <= 1:
        return n
    else:
        return fibonacci_get(n - 1) + fibonacci_get(n - 2)


new_number = int(input('Введите число последовательности ->'))
print(f'Ваше число: {fibonacci_get(new_number)}')
