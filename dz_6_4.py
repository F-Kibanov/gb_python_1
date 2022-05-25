from random import choice, randint


# Подготовка файлов hobby.csv и users.csv
def names_gen(name: str) -> list:
    """
    Генерирует список имен из исходного списка name_list по типу
    Иван -> Иванов Иван Иванович,
    выбирая фамилии и отчества случайным образом.

    """
    surname = f'{choice(name_list) + "ов, "}'
    patronymic = f'{choice(name_list) + "ович"}'
    name = f'{name + ", "}'

    name_one_str = [surname, name, patronymic + '\n']
    return name_one_str


name_list = ['Иван', 'Семен', 'Борис', 'Ильдар', 'Потап', 'Денис', 'Егор', 'Владимир', 'Юлиан', 'Бенедикт'] * 10
with open('users.csv', 'w', encoding='utf-8') as f:
    for name in name_list:
        f.writelines(names_gen(name))


def get_hobbies():
    """
    Возвращет случайное количество хобби в одной строке в установленных
    границах из двух слов (по одному из каждого списка).

    """
    verbs = ['ралли', 'бег', 'стрельба', 'скололазание', 'боксирование', 'скачки', 'плавание', 'прыжки']
    adjectives = ['на выносливость', 'трусцой', 'наперегонки', 'по мишеням', 'галопом', 'брассом', 'верхом', 'в длину']
    hobbylist = []

    num_hobbies = randint(1, 4)                         # Количество хобби в одной строке
    while num_hobbies:
        if num_hobbies - 1:
            word_1 = choice(verbs)
            word_2 = choice(adjectives)
            hobby = f'{word_1} {word_2}, '
            num_hobbies -= 1
            hobbylist.append(hobby)
        else:
            word_1 = choice(verbs)
            word_2 = choice(adjectives)
            hobby = f'{word_1} {word_2}\n'
            hobbylist.append(hobby)
            return hobbylist


with open('hobby.csv', 'w', encoding='utf-8') as f:
    for n in range(100):                                  # Задаем количество срок с наборами хобби
        f.writelines(get_hobbies())


def prepare_dataset(path_users_file: str, path_hobby_file: str):
    """
    Построчно считывает данные из файлов users.csv и hobby.csv и записывает их в файл users_hobby.txt через двоеточие.
    """

    users = open(path_users_file, 'r', encoding='utf-8')
    hobby = open(path_hobby_file, 'r', encoding='utf-8')
    res_file = open('users_hobby.txt', 'w', encoding='utf-8')
    line = users.readline()
    while line:
        res_line = str(line).strip('\n') + ': ' + (str(hobby.readline())).strip('\n')
        print(res_line, end='\n', file=res_file)
        line = users.readline()

    users.close()
    hobby.close()
    res_file.close()


prepare_dataset('users.csv', 'hobby.csv')
