# Задача 12: Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

from random import randint



def petya_number_give(n):
    n1 = randint(1, n)
    n2 = randint(1, n)
    return n1 + n2, n1 * n2


def katya_help(sum_and_multi):
    for i in range(1000):
        for j in range(1000):
            if i+j == sum_and_multi[0] and i*j == sum_and_multi[1]:
                n1 = i
                n2 =j
                return n1, n2


# Знаю что способ очень ресурсозатратный, но хотелось посмотреть сработает ли через цикл в цикле

petr_numbers = petya_number_give(1000)
print(f'Сумма чисел равна: {petr_numbers[0]}, а произведение равно: {petr_numbers[1]}')
katya_cheater = katya_help(petr_numbers)
print(f'Первое число: {katya_cheater[0]}, второе число: {katya_cheater[1]}')

