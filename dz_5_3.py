tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']  # 'Иван', 'Анастасия', 'Петр', 'Сергей']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    pass

    for _ in range(len(tutors)):
        try:
            result_tuple = (tutors[_], klasses[_])
            yield result_tuple
        except IndexError:
            result_tuple = (tutors[_], None)
            yield result_tuple


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))

for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
