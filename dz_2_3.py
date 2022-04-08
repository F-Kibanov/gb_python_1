def convert_list_in_str(my_list: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""

    str_out = ' '
    for i in range(len(my_list)):
        if my_list[i].isdigit():
            str_out += '"'
            str_out += my_list[i].zfill(2)
            str_out += '" '
        elif my_list[i].startswith('+' or '-'):
            str_out += '"'
            str_out += my_list[i].zfill(3)
            str_out += '" '
        else:
            str_out += my_list[i]
            str_out += ' '

    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
