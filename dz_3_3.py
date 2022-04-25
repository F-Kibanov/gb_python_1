def thesaurus(*args) -> dict:
    dict_out = {}
    for _ in range(len(args)):
        name = args[_]
        first_letter = name[0]
        dict_out_temp = {first_letter: [name]}
        if dict_out.get(first_letter):
            dict_out[first_letter].append(name)
        else:
            dict_out.update(dict_out_temp)

    # dict_out = {}  # результирующий словарь значений
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
