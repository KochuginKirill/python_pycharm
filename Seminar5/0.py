# #  посчитаем сумму всех чисел от 1 до N, N вводит юзер

# def summa_rec(num, upper):
#     # if num == 1:
#     #     return 1
#     # return num + summa_rec(num - 1 )
#     if num == upper:
#         return upper
#     return num + summa_rec(num + 1, upper )

# # процесс погружения (5 + (4 + (3 + (2 + ))))
# # процесс всплытия (5 + ( 4 + 6 )) = 15
# print(summa_rec(1, 1001))

def calc_count(sp):
    total = 0
    for el in sp:
        # if type(el) == type([]):
        if isinstance(el, list):
            total += calc_count(el)
        else:
            total += el
    return total




count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)
print(calc_count(count_all))