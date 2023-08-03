# Посчитать сумму цифр любого целого
# или вещественного числа,
# число вводит пользователь.
# Через строку решать нельзя.

number = float(input('Введите число'))
while number % 1 != 0:
    number *= 10
print(number)
sum = 0
while number != 0:
    sum += number % 10
    number //= 10
print(f'сумма равна:  {int(sum)}')