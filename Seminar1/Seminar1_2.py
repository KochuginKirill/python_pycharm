#Задача №3. Решение в группах
#В некоторой школе решили набрать три новых
#математических класса и оборудовать кабинеты для
#них новыми партами. За каждой партой может сидеть
#два учащихся. Известно количество учащихся в
#каждом из трех классов. Выведите наименьшее
#число парт, которое нужно приобрести для них.
#Input: 20 21 22(ввод чисел НЕ в одну строку)
#Output: 32

k1 = int(input("Введите сколько учеников в первом классе: "))
k2 = int(input("Введите сколько учеников во втором классе: "))
k3 = int(input("Введите сколько учеников в третьем классе: "))
i = 2
p1 = k1 // i + k1 % i
p2 = k2 // i + k2 % i
p3 = k3 // i + k3 % i
print(p1 + p2 + p3)

sum = 0
for i in (k1,k2,k3):
    sum+= i // 2 + i % 2
print(sum)