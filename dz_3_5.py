def get_jokes(n=5, repeats=True, **kwargs):
    """
    Составляет заданное количество шуток из трех слов, по одному из каждого списка.
    Если флаг repeats принимает значение True, то разрешается повтор слов в одной
    серии шуток, при значении False каждое слово будет использоваться только один раз.
    В качестве аргумента kwargs можно передать свои слова в формате 'group'=['word'].
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "послезавтра", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    for group, word in kwargs.items():
        if group == 'nouns':
            nouns.extend(word)
        elif group == 'adverbs':
            adverbs.extend(word)
        elif group == 'adjectives':
            adjectives.extend(word)
        else:
            print('wrong value added word!')

    from random import choice

    if repeats:
        for _ in range(n):
            word_1 = choice(nouns)
            word_2 = choice(adverbs)
            word_3 = choice(adjectives)
            joke = f'{word_1} {word_2} {word_3}'
            print(joke)
    else:
        min_len = min(len(nouns), len(adverbs), len(adjectives))
        if n > min_len:
            print('max number of original jokes is', min_len)
        else:
            for _ in range(n):
                word_1 = choice(nouns)
                nouns.remove(word_1)
                word_2 = choice(adverbs)
                adverbs.remove(word_2)
                word_3 = choice(adjectives)
                adjectives.remove(word_3)
                joke = f'{word_1} {word_2} {word_3}'
                print(joke)


get_jokes(7, repeats=False, nouns=['питон', 'кот'], adverbs=['днем', 'утром'], adjectives=['рыжий', 'водный'])
