def convert_name_extract(list_in: list) -> list:
    """Извлекает имена из элементов и формирует список приветствий."""

    for _ in range(len(list_in)):
        title_name = list_in[_].split()
        title_name = title_name.pop()
        title_name = title_name.title()
        greeting = f'Привет, {title_name}!'
        list_in[_] = greeting
    return list_in

    # list_out = ["здесь должены оказаться результирующие строковые приветствия"]
    # return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
