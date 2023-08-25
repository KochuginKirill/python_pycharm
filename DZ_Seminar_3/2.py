# Требуется найти в массиве list_1 самый близкий по величине элемент
# к заданному числу k и вывести его.
#
# Пример:
#
#
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 2, 3, 4, 5]
k = 6
result = 0
list_of_counts = []
for i in list_1:
    if i < k:
        list_of_counts.append(k-i)
    else:
        list_of_counts.append(i-k)

result = list_1[(list_of_counts.index(min(list_of_counts)))]
print(result)

