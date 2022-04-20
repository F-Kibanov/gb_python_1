def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    if number < 0:
        return 'wrong value!'
    elif number == 1 or number % 10 == 1 and number != 11:
        procents = (f'{number} процент')
    elif (1 < ((n % 10) or n) < 5) and n // 10 != 1:
        procents = (f'{number} процента')
    else:
        procents = (f'{number} процентов')
    return procents


for n in range(1, 101):                     # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))
