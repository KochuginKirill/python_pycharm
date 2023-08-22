# Задача 1
# HARD по желанию Напишите программу,
# которая принимает на вход целое или дробное число
# и выдаёт количество цифр в числе.
# 456 -> 3
# 0 -> 1
# 89,126 -> 5
# 0,001->4

def number_count(n):
    try:
        n = float(n)
    except ValueError:
        print('Вы ввели не число')
        exit()
    n = float(n)
    count = 0
    while n % 1 != 0:
        n *= 10
    while n > 0:
        n //= 10
        count += 1
    return count


number = input('Введите число (если число дробное, то вводите через ".") ->')
print(number_count(number))
