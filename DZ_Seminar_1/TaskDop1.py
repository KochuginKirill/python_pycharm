# Посчитать сумму цифр любого целого
# или вещественного числа,
# число вводит пользователь.
# Через строку решать нельзя.

try:
    number = float(input('Введите число => '))
except ValueError:
    print('Вы ввели не число')
    exit()

number = float(number)

while number % 1 != 0:
    number *= 10
sum = 0
while number != 0:
    sum += number % 10
    number //= 10
print(f'сумма равна:  {int(sum)}')