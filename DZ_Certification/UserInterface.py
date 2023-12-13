from easygui import *

from DZ_Certification import Notes

while True:
    user_input = enterbox('''1 - Напечатать заметки в терминале
2 - Добавить заметку
3 - Найти заметку
4 - Изменить заметку
5 - Удалить заметку
6 - Отсортированный по дате вывод
    (от самого нового)
7 - Выход''', 'Введите цифру запроса')
    user_input = Notes.try_int_get(user_input)
    if user_input == 1:
        try:
            Notes.show_notes()
        except FileNotFoundError:
            msgbox("Файл не найден, воспользуйтесь функцией добавления заметки для его создания (2)")
    elif user_input == 2:
        Notes.add_note()
    elif user_input == 3:
        try:
            Notes.search_note()
        except FileNotFoundError:
            msgbox("Файл не найден, воспользуйтесь функцией добавления заметки для его создания (2)")
    elif user_input == 4:
        try:
            Notes.change_note()
        except FileNotFoundError:
            msgbox("Файл не найден, воспользуйтесь функцией добавления заметки для его создания (2)")
    elif user_input == 5:
        try:
            Notes.delete_note()
        except FileNotFoundError:
            msgbox("Файл не найден, воспользуйтесь функцией добавления заметки для его создания (2)")
    elif user_input == 6:
        try:
            Notes.show_sorted_by_date()
        except FileNotFoundError:
            msgbox("Файл не найден, воспользуйтесь функцией добавления заметки для его создания (2)")
    elif user_input == 7:
        break
