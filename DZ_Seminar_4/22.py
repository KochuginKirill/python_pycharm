# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

def get_list(text):
    new_list = []
    print(text)
    list_element_counter = input('-> ')
    try:
        list_element_counter = int(list_element_counter)
    except ValueError:
        print('Вы ввели не число')
        exit()
    list_element_counter = int(list_element_counter)
    i = 0
    while i < list_element_counter:
        new_list.append(input(f'Введите {i + 1} элемент данного массива ->'))
        try:
            new_list[i] = int(new_list[i])
        except ValueError:
            print('Вы ввели не число')
            exit()
        new_list[i] = int(new_list[i])
        i += 1
    return new_list


def get_lists_similarities(list1, list2):
    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    return sorted(set(result))


first_list = get_list('Введите число элементов первого списка')
second_list = get_list('Введите число элементов второго списка')
print('Первый список:')
print(first_list)
print('Второй список:')
print(second_list)
result_list = get_lists_similarities(first_list, second_list)
print('Общие элементы:')
print(result_list)
