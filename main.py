# Программа меню.
from datetime import datetime, timedelta
import json
from pprint import pprint


def menu():
    # print(f"\033[2m\033[31m{"1. Внимание !!!! Удаление файла заметок."}\033[0m")
    print("1. Поиск заметки по заголовку.")
    print("2. Добавление новой заметки.")
    print("3. Удаление заметки(по заголовку).")
    print("4. Вывод всех записей из файла.")
    print("5. Замена записи, по заголовку.")
    print("0. Выход из программы.")


def razdel():
    print("--------------------------------------------")


def save(heading, body):  # Сохранение заметки
    try:
        new_data = {"heading": heading, "text": body, "data": str(datetime.now().strftime('%d/%m/%Y %H:%M:%S'))}
        with open("filedata.json", encoding="utf-8") as loadfile:
            data = json.load(loadfile)
            data["note"].append(new_data)
            with open("filedata.json", "w", encoding="utf-8") as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=2)
        razdel()


    except:
        print("Ошибка при работе с файлом")


def heading(heading_1):  # Поиск заметки по заголовку
    try:
        with open("filedata.json", encoding="utf-8") as file:
            data = json.load(file)
            razdel()
            # print(data["note"][0]["text"])
            i = 0
            for txt in data["note"]:
                if txt["heading"] == heading_1:
                    print(data["note"][i])
                else:
                    None
                i = i + 1
    except:
        print("Ошибка при работе с файлом")


def delet(text_del):  # Удаление заметки
    with open("filedata.json", "r", encoding="utf-8") as d:
        data = json.load(d)
        i = 0
        for txt in data["note"]:
            if txt["heading"] == text_del:
                data["note"].pop(i)
            else:  # Если нет совпадения
                None
            i = i + 1
        with open("filedata.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)


def outInput():  # Вывод всех записей в файле.
    print("Заголовок : Текст заметки : Дата и время создания заметки")
    with open("filedata.json", "r", encoding="utf-8") as savefile:
        data = json.load(savefile)
        # razdel()
    for txt in data["note"]:
        print(txt['heading'] + " : " + txt['text'] + " : " + txt['data'])
    razdel()


menu()
option = int(input("Введите номер команды из меню: "))
razdel()
while option != 0:
    if option == 1:  # Поиск заметки.
        heading_1 = str(input("Введите заголовок заметки: "))
        heading(heading_1)
        razdel()
    elif option == 2:  # Сохранение заметки с записью.
        heading = str(input("Введите заголовок заметки: "))
        body = str(input("Введите текст заметки: "))
        save(heading, body)
    elif option == 3:  # Удаление записи
        text_del = str(input("Введите запись для удаления: "))
        delet(text_del)
        #    with open("filedata.json", "w", encoding="utf-8") as f:
        #        json.dump(data, f, ensure_ascii=False, indent=2)
    elif option == 4:  # Вывод полного списка файла.
        outInput()
    elif option == 5:  # Замена записи
        heading_1 = input("Введите заголовок редактируемой заметки: ")
        outInput()
        body = input("Введите новый текст заметки: ")
        text_del = heading_1
        delet(heading_1)
        save(heading_1, body)
    else:
        print("Ввели не то!!!!!")
    menu()
    option = int(input("Введите номер команды из меню:"))
    razdel()

print("Программка отработала!!!!")
