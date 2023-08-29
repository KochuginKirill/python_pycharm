# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном списке урожайности грядки
#
# 4 -> 1 2 3 4
# 9

def get_berries(text):
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
        new_list.append(input(f'Введите чсило ягод {i + 1} куста ->'))
        try:
            new_list[i] = int(new_list[i])
        except ValueError:
            print('Вы ввели не число')
            exit()
        new_list[i] = int(new_list[i])
        i += 1
    return new_list


def get_best_raid(input_list):
    i = 3
    if len(input_list) < 2:
        print('Число кустов не должно быть меньше трех для подсчета')
        exit()
    maximum = input_list[0] + input_list[1] + input_list[2]
    while i < len(input_list):
        if input_list[i - 2] + input_list[i - 1] + input_list[i] > maximum:
            maximum = input_list[i - 2] + input_list[i - 1] + input_list[i]
        i += 1
    if input_list[len(input_list) - 2] + input_list[len(input_list) - 1] + input_list[0] > maximum:
        maximum = input_list[len(input_list) - 2] + input_list[len(input_list) - 1] + input_list[0]
    if input_list[len(input_list) - 1] + input_list[0] + input_list[1] > maximum:
        maximum = input_list[len(input_list) - 1] + input_list[0] + input_list[1]
    return maximum


berries_list = get_berries('Введите число кустов')
print(f'Ваши кусты:')
print(berries_list)
print('Максимальное число ягод за один заход:')
print(get_best_raid(berries_list))
