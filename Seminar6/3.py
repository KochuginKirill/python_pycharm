# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:
# 1 2 3 2 3
# Вывод:
# 2

from random import randint


def find_equal_count(input_list):
    sum = 0
    list_unique = set(input_list)
    for i in list_unique:
        sum += sp.count(i)//2
    return sum


# def find_eqal(input_list):
#     count = 0
#     res = 0
#     unique_list = set(input_list)
#     list(input_list)
#     for i in unique_list:
#         count = input_list.count(i)
#         if count > 1:
#             res += 1
#     return res


list_length = int(input('Введите число элементов массива ->'))
print(sp := [randint(1, 10) for x in range(list_length)])
result = find_equal_count(sp)
print(result)
