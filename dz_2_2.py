def convert_list_in_str(my_list: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""

    for i in range(len(my_list) - 1, 0, -1):
        if my_list[i].isdigit():
            my_list[i] = my_list[i].zfill(2)
            my_list.insert(i, '"'), my_list.insert(i + 2, '"')
        elif my_list[i].startswith('+' or '-'):
            my_list[i] = my_list[i].zfill(3)
            my_list.insert(i, '"'), my_list.insert(i + 2, '"')

    print(my_list)  # обработанный список

    str_out = ''
    for j in range(len(my_list)):
        if my_list[j].isdigit() or my_list[j] == '"' or my_list[j].startswith ('+' or '-'):
            str_out += ''
            str_out += my_list[j]
            str_out += ''
        else:
            str_out += ' '
            str_out += my_list[j]
            str_out += ' '

    return str_out



my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
