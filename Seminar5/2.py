# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1


def grade_downgrade_get(list_input):
    for i in range(len(list_input)):
        if list_input[i] == max(list_input):
            list_input[i] = min(list_input)
    return list_input


a = [1, 3, 3, 3, 4]
print(grade_downgrade_get(a))
