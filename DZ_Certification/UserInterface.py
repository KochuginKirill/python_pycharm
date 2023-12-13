from easygui import *

from DZ_Certification import Notes

while True:
    user_input = enterbox('''1 - Напечатать заметки в терминале
2 - Добавить заметку
3 - Найти заметку
4 - Изменить заметку
5 - Удалить заметку
6 - выход''', 'Введите цифру запроса')
    user_input = Notes.try_int_get(user_input)
    if user_input == 1:
        try:
            Notes.show_notes()
        except FileNotFoundError:
            msgbox("Файл не найден, воспользуйтесь функцией добавления заметки для его создания (2)")
    elif user_input == 2:
        Notes.add_note()
    elif user_input == 3:
        Notes.search_note()
    elif user_input == 4:
        Notes.change_note()
    elif user_input == 5:
        Notes.delete_note()
    elif user_input == 6:
        break
