# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

def daily_temperature_input(n_days):
    temperaturs = []
    i = 0
    while i < n_days:
        temperaturs.append(int(input(f'Введите температуру день: {i + 1} ->')))
        i += 1
    return temperaturs


def longest_temperature_show(daily_temperature):
    current = []
    max_temp = current
    for i in daily_temperature:
        if i > 0:
            current.append(i)
        else:
            current = []
    if len(current) > len(max_temp):
        max_temp = current
    return len(max_temp)


n = daily_temperature_input(int(input('Введите число дней ->')))
print(longest_temperature_show(n))
