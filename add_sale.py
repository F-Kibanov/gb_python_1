def main(argv):
    """
    Сохраняет введенные значения продаж из терминала в файл bakery.csv,
    если ввести несколько продаж за раз, то они будут сохранены в порядке ввода

    """

    program, *sale = argv
    res_file = open('bakery.csv', 'a', encoding='utf-8')
    while sale:
        one_sale = float(sale.pop(0))
        if one_sale:
            print(one_sale, file=res_file)
        else:
            print('Input sale digit!')

    res_file.close()


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
