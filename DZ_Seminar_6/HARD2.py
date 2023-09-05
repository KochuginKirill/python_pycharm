# Задача XO необязательная.
# Сделайте игру крестики - нолики, человек должен играть с ботом, поле 3*3.
# Конечно, бот не должен ходить на занятые поля
# Если есть желание, то можете наделить бота псевдоинтеллектом,
# чтоб он ходил как можно ближе к своим занятым клеткам
# После каждого хода на экран должна выводиться текущая обстановка на поле.
# Например,
#
# |     |  Х |
# |     |  O |
# |     |  O |
import random
from easygui import *


def field_generator(text):
    print(text)
    field = [['|_|', '|_|', '|_|'], ['|_|', '|_|', '|_|'], ['|_|', '|_|', '|_|']]
    string_1 = ''.join(map(str, field[0][:]))
    string_2 = ''.join(map(str, field[1][:]))
    string_3 = ''.join(map(str, field[2][:]))
    msgbox(f"""{string_1}
{string_2}
{string_3}""", 'Поле')
    return field


def first_turn(text):
    print(text)
    first_turn_randomizer = random.randint(0, 1)
    if first_turn_randomizer == 0:
        print('Первым ходите вы')
        return True
    else:
        print('Первым ходит бот')
        return False


def try_int_get(number):
    try:
        number = int(number)
    except ValueError:
        msgbox('Вы ввели не натуральное число от, пора начинать заново')
        exit()
    if 0 > int(number) or int(number) > 3:
        msgbox('Ваше число не подходит диапозону от 0 до 2')
        exit()
    else:
        return int(number)


def bot_xo(field, turn):
        if [a[0] for a in field].count('|_|') == 0 and [a[1] for a in field].count('|_|') == 0 and [a[2] for a in field].count('|_|') == 0:
            string_1 = ''.join(map(str, field[0][:]))
            string_2 = ''.join(map(str, field[1][:]))
            string_3 = ''.join(map(str, field[2][:]))
            msgbox(f"""{string_1}
{string_2}
{string_3}""", 'поле')
            print('Ничья')
            msgbox('Ничья')
            exit()
        else:
            if turn:
                string_1 = ''.join(map(str, field[0][:]))
                string_2 = ''.join(map(str, field[1][:]))
                string_3 = ''.join(map(str, field[2][:]))
                string = enterbox(f"""{string_1}
{string_2}
{string_3}""", 'Введите номер строки, где будет Х', '')
                string = try_int_get(string)
                column = enterbox(f"""{string_1}
{string_2}
{string_3}""", 'Введите номер столбца, где будет Х', '')
                column = try_int_get(column)
                if field[string][column] == '|_|':
                    field[string][column] = '|X|'
                    string_1 = ''.join(map(str, field[0][:]))
                    string_2 = ''.join(map(str, field[1][:]))
                    string_3 = ''.join(map(str, field[2][:]))
                    msgbox(f"""{string_1}
{string_2}
{string_3}""", 'ход бота')
                    if field[:][0].count('|X|') == 3 or field[:][1].count('|X|') == 3 or field[:][2].count('|X|') == 3:
                        msgbox('Вы победили!')
                        exit()
                    if [a[0] for a in field].count('|X|') == 3 or [a[1] for a in field].count('|X|') == 3 or [a[2] for a
                                                                                                              in
                                                                                                              field].count(
                        '|X|') == 3:
                        msgbox('Вы победили!')
                        exit()
                    if field[0][0] == '|X|' and field[1][1] == '|X|' and field[2][2] == '|X|':
                        msgbox('Вы победили!')
                        exit()
                    if field[0][2] == '|X|' and field[1][1] == '|X|' and field[2][0] == '|X|':
                        msgbox('Вы победили!')
                        exit()
                    turn = False
                    return bot_xo(field, turn)
                else:
                    msgbox('Нарушать правила не хорошо, бот покидает вас с разочарованием')
                    exit()
            else:
                if field[1][1] != '|X|' and field[1][1] != '|0|':
                    field[1][1] = '|0|'
                    print('первый ход бота: ')
                    string_1 = ''.join(map(str, field[0][:]))
                    string_2 = ''.join(map(str, field[1][:]))
                    string_3 = ''.join(map(str, field[2][:]))
                    msgbox(f"""{string_1}
{string_2}
{string_3}""", 'следующий ход')
                    turn = True
                    return bot_xo(field, turn)
                else:
                    try_turn = 'check'
                    while try_turn != '|_|':
                        random_string = random.randint(0, 2)
                        random_column = random.randint(0, 2)
                        try_turn = field[random_string][random_column]
                        if try_turn == '|_|':
                            field[random_string][random_column] = '|0|'
                            print('ход бота: ')
                            string_1 = ''.join(map(str, field[0][:]))
                            string_2 = ''.join(map(str, field[1][:]))
                            string_3 = ''.join(map(str, field[2][:]))
                            msgbox(f"""{string_1}
{string_2}
{string_3}""", 'теперь ход бота')
                            if field[:][0].count('|0|') == 3 or field[:][1].count('|0|') == 3 or field[:][2].count(
                                    '|0|') == 3:
                                msgbox('Бот победил!')
                                exit()
                            if [a[0] for a in field].count('|0|') == 3 or [a[1] for a in field].count('|0|') == 3 or [
                                a[2] for a in field].count('|0|') == 3:
                                msgbox('Бот победил!')
                                exit()
                            if field[0][0] == '|0|' and field[1][1] == '|0|' and field[2][2] == '|0|':
                                msgbox('Бот победил!')
                                exit()
                            if field[0][2] == '|0|' and field[1][1] == '|0|' and field[2][0] == '|0|':
                                msgbox('Бот победил!')
                                exit()
                            turn = True
                            return bot_xo(field, turn)


field_generated = field_generator('Ваше поле в окне:')
whos_turn = first_turn('Сейчас узнаем кто будет ходить первым, посмотрите в появившееся окно')
bot_xo(field_generated, whos_turn)
