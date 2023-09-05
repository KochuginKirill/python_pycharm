# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно
#
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

def get_index_range(list_input, minimum, maximum):
    result = [list_input.index(i) for i in list_input if minimum < i < maximum]
    return result


list_inputed = [1, 5, 88, 100, 2, -4]
result = get_index_range(list_inputed, 33,200)
print(result)
