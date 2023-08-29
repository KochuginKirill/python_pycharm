# задача 2 необязательная. Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.
# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно
# Используйте функции

def get_convert(input_int, number_system):
    allnumbers = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if number_system > input_int:
        return 'Перевести такое число не выйдет'
    result = ''
    while input_int > 0:
        result = allnumbers[input_int % number_system] + result
        input_int //= number_system
    return result


def try_int_get(number):
    try:
        number = int(number)
    except ValueError:
        print('Вы ввели не натуральное число')
        exit()
    return int(number)


number = input('Введите целое число -> ')
number = try_int_get(number)
number_system = input('Введите систему счисления целым числом -> ')
number_system = try_int_get(number_system)
result = get_convert(number, number_system)
print(result)
