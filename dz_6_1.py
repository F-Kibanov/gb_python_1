from pprint import pprint


def get_parse_attrs(line: str) -> tuple:
    """Парсит строку на атрибуты и возвращает кортеж атрибутов (<remote_addr>, <request_type>, <requested_resource>)"""

    for el in line[1:4]:
        if el == '.':
            list_temp = line.split()
            tuple_out = tuple([list_temp[0], list_temp[5].removeprefix('"'), list_temp[6]])
            return tuple_out
        else:
            pass
    # верните кортеж значений <remote_addr>, <request_type>, <requested_resource>


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    for line in fr:
        list_out.append(get_parse_attrs(line))
    # передавайте данные в функцию и наполняйте список list_out кортежами

    pprint(list_out)
