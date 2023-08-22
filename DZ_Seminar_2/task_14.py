# Задача 14:
# Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.

def degrees_of_2_show(n):
    if n < 0:
        return 'Число не может быть меньше 0, попробуйте еще раз'
    elif n == 0:
        return 1
    else:
        res = [1]
        current_degree = 1
        while current_degree <= n/2:
            current_degree *= 2
            res.append(current_degree)
        return res


output = degrees_of_2_show(int(input('Введите целое число -> ')))
print(f'Степени двойки ниже или равные  вашему числу: {output}')
