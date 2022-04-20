def sum_list_1(dataset: list) -> int:
    """Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7"""
    dataset = []
    for i in range(1, 1000, 2):
        dataset.append(i ** 3)
    sum_a = 0
    check_a = 0
    for number_a in dataset:
        count_a = 0
        check_a = number_a
        while check_a > 0:
            count_a += check_a % 10
            check_a = check_a // 10
        if count_a % 7 == 0:
            sum_a += number_a
    return sum_a                            # Верните значение полученной суммы
print(sum_list_1(1000))


def sum_list_2(dataset2: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
        сумма цифр которых делится нацело на 7"""
    dataset2 = []
    for j in range(1, 1000, 2):
        dataset2.append(j ** 3 + 17)
    sum_b = 0
    check_b = 0
    for number_b in dataset2:
        count_b = 0
        check_b = number_b
        while check_b > 0:
            count_b += check_b % 10
            check_b = check_b // 10
        if count_b % 7 == 0:
            sum_b += number_b
    return sum_b
print(sum_list_2(1000))
