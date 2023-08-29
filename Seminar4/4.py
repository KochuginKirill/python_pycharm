# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени,
# где все коэффициенты случайные от -10 до 10.
#
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0

import random


def generate_polynomial(k):
    coefficients = [random.randint(-10, 10) for _ in range(k + 1)]  # Генерируем случайные коэффициенты
    polynomial = ""

    # Формируем строковое представление многочлена
    for i, coeff in enumerate(coefficients):
        if coeff != 0:
            if i == 0:
                polynomial += str(coeff)
            else:
                polynomial += " + " if coeff > 0 else " - "
                polynomial += str(abs(coeff))
                if i > 1:
                    polynomial += "*x^{}".format(i)
                else:
                    polynomial += "*x"

    polynomial += " = 0"  # Добавляем знак равенства

    return polynomial


k = int(input("Введите степень многочлена: "))
polynomial = generate_polynomial(k)
print(polynomial)