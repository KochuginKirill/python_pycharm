from easygui import *
import re
import datetime as DT
from datetime import datetime


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
            parts = temp[i].split(";")
            print(f'''----------------------------------------------------
№{counter}
{parts[0]}
{parts[1]}
{parts[2]}
{parts[3]}
----------------------------------------------------''')
            counter += 1

    data.close()


def add_note():
    data = open('notes.json', 'a', encoding = "UTF-8")
    data.close()
    data = open('notes.json', 'r', encoding = "UTF-8")
    temp = sorted(data.readlines())
    counter = 0
    for i in range(len(temp)):
        if len(temp[i]) > 0:
            parts = temp[i].split(";")
            partOfPart = parts[0].split(" ")
            counter = int(partOfPart[1]) + 1
    data.close()
    data = open('notes.json', 'a', encoding = "UTF-8")
    title = enterbox('Введите название заметки')
    text = enterbox('Введите заметку')
    data.writelines(f'''id: {counter}; Заголовок: {title}; Текст: {text};{DT.datetime.today()}; 
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
        parts = result.split(";")
        msgbox(f'''Нашлась следующая заметка: {parts[0]}
{parts[1]}
{parts[2]}
{parts[3]}''')
    else:
        msgbox('Такая заметка не найдена')
        data.close()


def change_note():
    data = open('notes.json', 'r', encoding = "UTF-8")
    search = enterbox('Введите название или часть текста заметки, которую хотите изменить')
    result = ''
    id = -1
    for line in data:
        if search.lower() in line.lower():
            result = line
    if len(result) > 0:
        parts = result.split(";")
        msgbox(f'''Нашлась следующая заметка: {parts[0]}
        {parts[1]}
        {parts[2]}
        {parts[3]}''')
        partId = parts[0].split(" ")
        id = partId[1]
    else:
        msgbox('Элемент не найден')
    data.close()
    if len(result) > 0:
        title = enterbox('Введите новое название')
        text = enterbox('Введите новую заметку')
        input_result = (f'''id: {id}; Заголовок: {title}; Текст: {text};{DT.datetime.today()}; 
''')
        with open('notes.json', 'r', encoding = "UTF-8") as dana_inputed:
            old_data = dana_inputed.read()
        new_data = old_data.replace(f'{result}', f'{input_result}')
        with open('notes.json', 'w', encoding = "UTF-8") as dana_inputed:
            dana_inputed.write(new_data)


def delete_note():
    data = open('notes.json', 'r', encoding = "UTF-8")
    search = enterbox('Введите заголовок или часть текста заметки, которую хотите удалить')
    result = ''
    for line in data:
        if search.lower() in line.lower():
            result = line
    if len(result) > 0:
        parts = result.split(";")
        msgbox(f'''Нашлась следующая заметка: {parts[0]}
        {parts[1]}
        {parts[2]}
        {parts[3]}''')
    else:
        msgbox('Элемент для удаления не найден')
    data.close()
    if len(result) > 0:
        with open('notes.json', encoding = "UTF-8") as notes:
            lines = notes.readlines()
        pattern = re.compile(re.escape(result))
        with open('notes.json', 'w', encoding = "UTF-8") as notes:
            for line in lines:
                result = pattern.search(line)
                if result is None:
                    notes.write(line)
        notes.close()
        msgbox('Элемент удален')


def show_sorted_by_date():
    print('==========================================================')
    data = open('notes.json', 'r', encoding = "UTF-8")
    temp = sorted(data.readlines())
    copyTemp = temp
    maxDate = DT.datetime.min
    for k in range(len(temp)):
        for i in range(len(copyTemp)):
            if len(copyTemp[i]) > 0:
                if copyTemp[i] != "просмотрено":
                    parts = copyTemp[i].split(";")
                    dateCheck = datetime.strptime(parts[3], '%Y-%m-%d %H:%M:%S.%f')
                    if dateCheck > maxDate:
                        maxDate = dateCheck
        for j in range(len(temp)):
            if len(copyTemp[i]) > 0:
                if temp[j] != "просмотрено":
                    parts = temp[j].split(";")
                    if datetime.strptime(parts[3], '%Y-%m-%d %H:%M:%S.%f') == maxDate:
                        print(f'''----------------------------------------------------
{parts[0]}
{parts[1]}
{parts[2]}
{parts[3]}
----------------------------------------------------''')
                        copyTemp[j] = "просмотрено"
                        maxDate = DT.datetime.min
                        continue
    data.close()
