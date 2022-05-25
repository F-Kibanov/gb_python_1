from itertools import islice


def main(argv):
    """
    Выводит  значения продаж из файла bakery.csv в теримнал,
    в качестве аргументов принимаются номера строк,
    которые нужно вывести

    """

    program, *sale = argv
    res_file = open('bakery.csv', 'r', encoding='utf-8')
    result = list(map(int, sys.argv[1:]))

    if len(result) == 1:
        first_number = int(result[0]) - 1
        print(*islice(res_file, first_number, None))
    elif len(result) == 2:
        first_number = int(result[0]) - 1
        second_number = int(result[1])
        print(*islice(res_file, first_number, second_number))
    else:
        line = res_file.readline()
        while line:
            print(line.strip('\n'))
            line = res_file.readline()

    res_file.close()


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
