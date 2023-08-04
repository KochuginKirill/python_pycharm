# Задача 2:
# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input('Введите целое число => ')
intCheck = number.isdigit()
if not intCheck:
    print('Вы ввели не целое число')
else:
    number = int(number)
    sum = int(0)
    while number > 0:
        sum += number %10
        number //= 10
    print(f'Сумма чисел равна {sum}')