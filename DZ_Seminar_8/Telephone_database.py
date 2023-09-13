from easygui import *
import re


def try_int_get(number):
    try:
        number = int(number)
    except ValueError:
        msgbox('Вы ввели не число')
        exit()
    return int(number)


def show_phonebook():
    print('==========================================================')
    data = open('BD_phonebook.txt', 'r', encoding = "UTF-8")
    temp = sorted(data.readlines())
    counter = 1
    for i in range(len(temp)):
        if len(temp[i]) > 0:
            print(f'{counter}. {temp[i]}')
            counter += 1
    data.close()


def add_line_phonebook():
    data = open('BD_phonebook.txt', 'a', encoding = "UTF-8")
    new_name = enterbox('Введите название нового контакта')
    new_number = enterbox('Введите норер(а) нового контакта')
    data.writelines(f'''
{new_name} {new_number}''')
    data.close()


def search_line_phonebook():
    data = open('BD_phonebook.txt', 'r', encoding = "UTF-8")
    search = enterbox('Введите имя или телефон того, кого хотите найти')
    result = ''
    for line in data:
        if search.lower() in line.lower():
            result = line
    if len(result) > 0:
        msgbox(f'Нашелся: {result}')
    else:
        msgbox('Такой контакт не найден')
        data.close()


def change_line_phonebook():
    data = open('BD_phonebook.txt', 'r', encoding = "UTF-8")
    search = enterbox('Введите имя или телефон того, кого хотите изменить')
    result = ''
    for line in data:
        if search.lower() in line.lower():
            result = line
    if len(result) > 0:
        msgbox(f'Найден следующий элемент {result}')
    else:
        msgbox('Элемент для удаления не найден')
    data.close()
    if len(result) > 0:
        new_name = enterbox('Введите новое имя')
        new_telephone = enterbox('Введите новый телефон(ы)')
        input_result = new_name + ' ' + new_telephone
        with open('BD_phonebook.txt', 'r', encoding = "UTF-8") as dana_inputed:
            old_data = dana_inputed.read()
        new_data = old_data.replace(f'{result}', f'{input_result}')
        with open('BD_phonebook.txt', 'w', encoding = "UTF-8") as dana_inputed:
            dana_inputed.write(new_data)


def delete_line_phonebook():
    data = open('BD_phonebook.txt', 'r', encoding = "UTF-8")
    search = enterbox('Введите имя или телефон того, кого хотите удалить')
    result = ''
    for line in data:
        if search.lower() in line.lower():
            result = line
    if len(result) > 0:
        msgbox(f'Найден следующий элемент {result}')
    else:
        msgbox('Элемент для удаления не найден')
    data.close()
    if len(result) > 0:
        with open('BD_phonebook.txt', encoding = "UTF-8") as BD_phonebook:
            lines = BD_phonebook.readlines()
        pattern = re.compile(re.escape(result))
        with open('BD_phonebook.txt', 'w', encoding = "UTF-8") as BD_phonebook:
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    BD_phonebook.write(line)
        BD_phonebook.close()
        msgbox('Элемент удален')



while True:
    user_input = enterbox('''1 - Напечатать телефонную книгу в терминале
2 - Добавить контакт в  телефонной книге
3 - Найти контакт в телефонной книге
4 - Изменить контакт в телефонной книге
5 - Удалить контакт в телефонной книге
6 - выход''', 'Введите цифру запроса')
    user_input = try_int_get(user_input)
    if user_input == 1:
        show_phonebook()
    elif user_input == 2:
        add_line_phonebook()
    elif user_input == 3:
        search_line_phonebook()
    elif user_input == 4:
        change_line_phonebook()
    elif user_input == 5:
        delete_line_phonebook()
    elif user_input == 6:
          break