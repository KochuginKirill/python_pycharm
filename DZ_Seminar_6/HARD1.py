# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
#
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

def nega_fibonachi(number):
    list_result = [0]
    for i in range(1, number + 1):
        if i == 1:
            list_result.insert(0, -i)
            list_result.append(i)
        else:
            list_result.insert(0, list_result[0] + list_result[1])
            list_result.append(list_result[len(list_result) - 1] + list_result[len(list_result) - 2])
    return list_result


def try_int_get(number):
    try:
        number = int(number)
    except ValueError:
        print('Вы ввели не натуральное число')
        exit()
    return int(number)


number_user = input('Введите количество чисел для ряда фибоначи -> ')
number_user = try_int_get(number_user)
print(nega_fibonachi(number_user))
