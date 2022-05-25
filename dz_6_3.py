import json
from random import choice, randint
import itertools as it


# Подготовка файлов hobby.csv и users.csv
def names_gen(name: str) -> list:
    """
    Генерирует список имен из исходного списка по типу
    Иван -> Иванов Иван Иванович,
    выбирая фамилии и отчества случайным образом.

    """
    surname = f'{choice(name_list) + "ов, "}'
    patronymic = f'{choice(name_list) + "ович"}'
    name = f'{name + ", "}'

    name_one_str = [surname, name, patronymic + '\n']
    return name_one_str


name_list = ['Иван', 'Семен', 'Борис', 'Ильдар', 'Потап', 'Денис', 'Егор', 'Владимир', 'Юлиан', 'Бенедикт']
with open('users.csv', 'w', encoding='utf-8') as f:
    for name in name_list:
        f.writelines(names_gen(name))


def get_hobbies():
    """
    Возвращет случайное количество хобби в границах от одного до четырех из двух слов (по одному из каждого списка).
    """

    verbs = ['ралли', 'бег', 'стрельба', 'скололазание', 'боксирование', 'скачки', 'плавание', 'прыжки']
    adjectives = ['на выносливость', 'трусцой', 'наперегонки', 'по мишеням', 'галопом', 'брассом', 'верхом', 'в длину']
    hobbylist = []

    num_hobs = randint(1, 4)                            # Количество хобби в одной строке
    while num_hobs:
        if num_hobs - 1:
            word_1 = choice(verbs)
            word_2 = choice(adjectives)
            hobby = f'{word_1} {word_2}, '
            num_hobs -= 1
            hobbylist.append(hobby)
        else:
            word_1 = choice(verbs)
            word_2 = choice(adjectives)
            hobby = f'{word_1} {word_2}\n'
            hobbylist.append(hobby)
            return hobbylist


with open('hobby.csv', 'w', encoding='utf-8') as f:
    for n in range(8):                                   # Задаем количество срок с наборами хобби
        f.writelines(get_hobbies())


def prepare_dataset(path_users_file: str, path_hobby_file: str) -> dict:
    """
    Считывает данные из файлов и возвращает словарь, где:
        ключ — ФИО, значение — данные о хобби (список строковых переменных)
    :param path_users_file: путь до файла, содержащий ФИО пользователей, разделенных запятой по строке
    :param path_hobby_file: путь до файла, содержащий хобби, разделенные запятой по строке
    :return: Dict(str: Union[List[str]|None])
    """

    user_temp = []
    with open(path_users_file, 'r', encoding='utf-8') as users:
        for users_line in users:
            user_temp.append(users_line.strip())

    hobby_temp = []
    with open(path_hobby_file, 'r', encoding='utf-8') as hobby:
        for hobby_line in hobby:
            hobby_temp.append(hobby_line.strip())

    dict_out = {}
    if len(hobby_temp) <= len(user_temp):
        if hobby_temp:
            dict_out = dict(it.zip_longest(user_temp, hobby_temp))
        else:
            dict_out.setdefault(user_temp)
    else:
        quit(1)

    return dict_out                 # верните словарь, либо завершите исполнение программы кодом 1


dict_out = prepare_dataset('users.csv', 'hobby.csv')
with open('task_6_3_result.json', 'w', encoding='utf-8') as fw:
    json.dump(dict_out, fw, ensure_ascii=False, indent=2)
