# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def arithmetical_progression(a1, n, d): # первый элемент, разность, количество
    result_list = [a1]
    for i in range(d):
        a1 += a1 + (n-1) * d
        result_list.append(a1)
    return result_list


def try_int_get(number):
    try:
        number = int(number)
    except ValueError:
        print('Вы ввели не натуральное число')
        exit()
    return int(number)


a1 = input('Введите a1 -> ')
a1 = try_int_get(a1)
n = input('Введите n -> ')
n = try_int_get(n)
d = input('Введите d -> ')
d = try_int_get(d)
result = arithmetical_progression(a1, n,  d)
print(result)
