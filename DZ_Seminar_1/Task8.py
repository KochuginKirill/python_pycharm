# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no


a = input('Введите число долект по вертикали => ')
intCheck = a.isdigit()
if not intCheck:
    print('Вы ввели не целое число')
    exit()
else:
    a = int(a)
b = input('Введите число долект по вертикали => ')
intCheck = b.isdigit()
if not intCheck:
    print('Вы ввели не целое число')
    exit()
else:
    b = int(b)
c = input('Введите число долект по вертикали => ')
intCheck = c.isdigit()
if not intCheck:
    print('Вы ввели не целое число')
    exit()
else:
    c = int(c)
if c % a == 0 or c % b == 0:
    print("yes")
else:
    print('no')
