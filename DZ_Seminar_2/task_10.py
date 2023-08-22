# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random


def coin_show(number_coins):
    coin_on_table = []
    coin_sides = ['орел', 'решка']
    i = 0
    while i < number_coins:
        coin_on_table.append(random.choice(coin_sides))
        i += 1
    return coin_on_table


def min_tos_coin_show(coins):
    heads_count = 0
    tails_count = 0
    for i in coins:
        if i == 'орел':
            heads_count += 1
        else:
            tails_count += 1
    if heads_count < tails_count:
        return heads_count
    else:
        return tails_count  # Если они равны, то не важно какой count возвращать


coins_input = coin_show(int(input('Введите число монет -> ')))
print('Ваши монеты упали таким образом:')
print(coins_input)
result = min_tos_coin_show(coins_input)
print(f'Нужно перевернуть монет: {result}, чтобы они были одной стороной')

