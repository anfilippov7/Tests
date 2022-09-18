# def multiplication_int(a: int, b: int) -> int:
#     return a * b
import yadisk
import requests

# Задание №1

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

def name_people(people):
    for i in documents:
        if i.get("number") == people:
            resault_name = i.get("name")
            return f'Имя человека, которому принадлежит документ {people}: {resault_name}'

def name_shelf(shelf):
    for key, value in directories.items():
        for i in value:
            if i == shelf:  # сравниваем значение с введенным значением shelf которое передаем в функцию name_shelf(name) name это shelf
                return f'Номер полки, на которой находится документ {i}: {key}'
    else:
        return f'В базе данных нет такого документа'
        # return name_shelf.__name__

def name_list(documents):
    count = 0
    name_data = ''
    for value in documents:
        dict_values = list(value.values())
        count += 1
        name_data += f'Данные сотрудника № {count}: {dict_values}\n'
    return name_data

def name_add(number, type, name, num_directories):
    key_dict = directories.keys()
    count = 0
    for i in key_dict:
        if num_directories != i:
            count += 1
    if count == len(key_dict):
        return f"Нет такой полки!"
    add = {
        "type": type,
        "number": number,
        "name": name
    }
    directories.setdefault(num_directories, []).append(number)
    documents.append(add)
    return f'directories = {directories}\ndocuments = {documents}'

def name_delete(number_del):
    count = 0
    for i in documents:
        if number_del == i.get("number"):
            count += 1
            i.clear()
            for keys, values in directories.items():
                for i in values:
                    if i == number_del:
                        values.remove(number_del)
            return f'directories = {directories}\ndocuments = {documents}'
    if count == 0:
        return f"Вы вводите несуществующий документ!"

def name_movie(number_movie, number_rack):
    count = 0
    count2 = 0
    for keys, values in directories.items():
        for i in values:
            if i == number_movie:
                count += 1
        for i in keys:
            if i == number_rack:
                count2 += 1
    if count == 0:
        return f"Нет такого документа!"
    if count2 == 0:
        return f"Нет такой полки!"
    for keys, values in directories.items():
        for i in values:
            if i == number_movie:
                values_copy = values
                values_copy.remove(number_movie)
                directories.setdefault(number_rack, []).append(number_movie)
    return f'directories = {directories}'

def name_add_self(number_add_self):
    for keys in directories:
        if keys == number_add_self:
            return f"Данная полка уже существует!"
    else:
        directories.setdefault(number_add_self, [])
        return f'directories = {directories}'


# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     command = input("Введите команду: ")
#     if command == "p":
#         people = input("Введите номер документа: ")
#         print(name_people(people))  # вызываем фукцию name_man со значением введенной переменной
#     elif command == "s":
#         shelf = input("Введите номер документа: ")
#         print(name_shelf(shelf))  # вызываем фукцию name_shelf со значением введенной переменной
#     elif command == "l":
#         print(name_list(documents))
#     elif command == "a":
#         number = input("Введите номер документа: ")
#         type = input("Введите тип документа: ")
#         name = input("Введите имя: ")
#         num_directories = input("Введите номер полки: ")
#         print(name_add(number, type, name, num_directories))
#     elif command == "d":
#         number_del = input("Введите номер удаляемого документа: ")
#         print(name_delete(number_del))
#     elif command == "m":
#         number_movie = input("Введите номер документа: ")
#         number_rack = input("Введите номер полки для перемещения документа: ")
#         print(name_movie(number_movie, number_rack))
#     elif command == "as":
#         number_add_self = input("Введите номер полки: ")
#         print(name_add_self(number_add_self))


# Задание №2


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def put_folder(self, folder_name):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": folder_name}
        response = requests.put(files_url, params=params, headers=headers)
        # print('Папка создана')
        return response.status_code

    # def _get_upload_link(self, disk_file_path):
    #     upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
    #     headers = self.get_headers()
    #     params = {"path": disk_file_path, "overwrite": "true"}
    #     response = requests.get(upload_url, headers=headers, params=params)
    #     return response.json()

    # def upload_data_to_disk(self, disk_file_path, filename):
    #     href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
    #     response = requests.put(href, data=filename)

    # def upload_file_to_link(self, disk_file_path, url):
    #     href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
    #     response = requests.put(href, data=url)
    #     print(f"Файл {keys} загружен")


if __name__ == '__main__':
    # TOKEN = "AQAAAAAJ2UEnAADLW_g9FsGOjUm9koH-YGtzlMs"
    TOKEN = input("Введите токен Яндекс.Диск: ")
    # user_id = '17331357'
    check = yadisk.YaDisk(token=TOKEN)
    # Проверяет, валиден ли токен
    if check.check_token() == True:
        folder = input("Введите имя папки для сохранения фотографий: ")
        ya = YandexDisk(TOKEN)
        print(ya.put_folder(folder_name=folder))
        # ya.upload_data_to_disk(f"{folder}/data_foto.json", list_data_foto)
        # for keys, values in dictionary_foto.items():
        #     ya.upload_file_to_link(disk_file_path=f"{folder}/{keys}", url=values)
    else:
        print("Некорректный токен!")