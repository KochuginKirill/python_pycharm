# elif choice == "Загрузить БД":  #если выбрали этот пункт
#             # загрузить из json
#             fname=fileopenbox('Выберите файл формата JSON')  #открываем файл
#             with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
#                 BD = json.load(fh)  # загружаем из файла данные в словарь data
#             print('БД успещно загружена')
#             loaded=True #меняем флаг загрузки БД
#         elif choice=='Сохранить БД': #если выбрали этот пункт
#             # сохранить в json
#             with open('BD.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
#                 fh.write(json.dumps(BD,
#                                     ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
#             print('БД успещно сохранена')