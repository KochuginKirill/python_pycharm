from easygui import *
import re


def try_int_get(number):
    try:
        number = int(number)
    except ValueError:
        msgbox('Вы ввели не число')
        exit()
    return int(number)


def show_notes():
    print('==========================================================')
    data = open('notes.json', 'r', encoding = "UTF-8")
    temp = sorted(data.readlines())
    counter = 1
    for i in range(len(temp)):
        if len(temp[i]) > 0:
            print(f'№{counter}. Заметка: {temp[i]}')
            counter += 1
    data.close()


def add_note():
    data = open('notes.json', 'a', encoding = "UTF-8")
    title = enterbox('Введите название заметки')
    text = enterbox('Введите заметку')
    data.writelines(f'''Заголовок: {title}. Текст: {text}
''')
    data.close()


def search_note():
    data = open('notes.json', 'r', encoding = "UTF-8")
    search = enterbox('Введите имя или телефон того, кого хотите найти')
    result = ''
    for line in data:
        if search.lower() in line.lower():
            result = line
    if len(result) > 0:
        msgbox(f'Нашелся: {result}')
    else:
        msgbox('Такая заметка не найдена')
        data.close()


def change_note():
    data = open('notes.json', 'r', encoding = "UTF-8")
    search = enterbox('Введите название или часть текста заметки, которую хотите изменить')
    result = ''
    for line in data:
        if search.lower() in line.lower():
            result = line
    if len(result) > 0:
        msgbox(f'Найден следующий элемент {result}')
    else:
        msgbox('Элемент не найден')
    data.close()
    if len(result) > 0:
        new_name = enterbox('Введите новое название')
        new_telephone = enterbox('Введите новую заметку')
        input_result = new_name + ' ' + new_telephone
        with open('notes.json', 'r', encoding = "UTF-8") as dana_inputed:
            old_data = dana_inputed.read()
        new_data = old_data.replace(f'{result}', f'{input_result}')
        with open('notes.json', 'w', encoding = "UTF-8") as dana_inputed:
            dana_inputed.write(new_data)


def delete_note():
    data = open('notes.json', 'r', encoding = "UTF-8")
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
        with open('notes.json', encoding = "UTF-8") as BD_phonebook:
            lines = BD_phonebook.readlines()
        pattern = re.compile(re.escape(result))
        with open('notes.json', 'w', encoding = "UTF-8") as BD_phonebook:
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    BD_phonebook.write(line)
        BD_phonebook.close()
        msgbox('Элемент удален')