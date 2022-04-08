from random import uniform


def transfer_list_in_str(list_in: list) -> str:
    """Преобразует каждый элемент списка (вещественное число) в строку вида '<r> руб <kk> коп' и
        формирует из них единую строковую переменную разделяя значения запятой."""

    str_out = ' '
    for _ in range(len(my_list)):
        rub = str(round(my_list[_] // 1))
        kop = (str(round(my_list[_] % 1 * 100))).zfill(2)
        str_out += f'{rub} руб {kop} коп'
        if _ < len(my_list) - 1:
            str_out += ', '
    # str_out = "здесь итоговая строка"
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    """Сортирует вещественные числа по возрастанию, не создавая нового списка"""
    print('id original list = ', id(list_in))
    # зафиксируйте здесь информацию по исходному списку my_list
    list_in.sort()
    # зафиксируйте здесь доказательство, что результат result_2 остался тем же объектом
    print('id sorted list = ', id(list_in))
    # return ["отсортированный результирующий список"]
    return list_in


result_2 = sort_prices(my_list)
print('Цены по возрастанию, список тот же', result_2)


def sort_price_adv(list_in: list) -> list:
    """Создаёт новый список и возвращает список с элементами по убыванию"""
    print('my_list id = ', id(my_list))
    list_out = sorted(my_list, reverse=True)
    print('list_out id = ', id(list_out))
    # list_out = ["список элементов в списке по убыванию"]
    return list_out


result_3 = sort_price_adv(my_list)
print('Цены по убыванию, список новый', result_3)


def check_five_max_elements(list_in: list) -> list:
    """Проверяет элементы входного списка вещественных чисел и возвращает
        список из ПЯТИ максимальных значений"""

    list_out = sorted(list_in, reverse=True)[0: 5]
    # list_out = ["список из пяти самых больших элементов"]
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
