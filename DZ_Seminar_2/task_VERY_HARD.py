# Задача VERY HARD необязательная
# Имеется список случайных целых чисел.
# Создайте список, в который попадают числа,
# описывающие максимальную сплошную возрастающую последовательность.
# Порядок элементов менять нельзя.
# Одно число - это не последовательность.
#
# Пример:
#
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
# так как здесь вразброс присутствуют все числа от 1 до 7
#
# [1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
# так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8
#
# [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
# так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

from random import randint


def list_int_get(n, n_min, n_max):
    list_int = []
    i = 0
    while i < n:
        list_int.append(randint(n_min, n_max))
        i += 1
    return list_int


def longest_increasing_sequence_show(list_of_int):
    current_sequence = []
    max_sequence = current_sequence
    i = 1
    while i < len(list_of_int):
        if list_of_int[i] > list_of_int[i - 1]:
            if len(current_sequence) == 0:
                current_sequence.append(list_of_int[i - 1])
            current_sequence.append(list_of_int[i])
        else:
            if len(current_sequence) > len(max_sequence):
                max_sequence = current_sequence
            current_sequence = []
        i += 1
    if len(max_sequence) > 0:
        return max_sequence
    else:
        return 'Последовательность отсутствует'


n = int(input('Введите количество чисел -> '))
min_input = int(input('Введите минимальную границу для генерации случайных чисел -> '))
max_input = int(input('Введите максимальную границу для генерации случайных чисел -> '))
new_list = list_int_get(n, min_input, max_input)
print('Ваша последовательность:')
print(new_list)
result = longest_increasing_sequence_show(new_list)
print('Самая длинная возрастающая последовательность:')
print(result)
# Показывает первую последовательность, если есть несколько последовательностей одной длины
