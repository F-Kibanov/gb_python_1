def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    # реализуйте здесь, где хранить необходимые исходные данные определитесь самостоятельно

    eng_rus = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    if value[0].isupper():
        word = value.lower()
        word = (eng_rus.get(word))
        if word:
            str_out = word.title()
        else:
            str_out = word
    else:
        str_out = eng_rus.get(value)

    # str_out = "в этой переменной должен оказаться результат перевода"
    return str_out


print(num_translate("One"))
print(num_translate("eight"))
