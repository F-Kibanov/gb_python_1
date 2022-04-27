from sys import argv
from utils import currency_rates

if len(argv) > 1:
    print(currency_rates(argv[1]))
else:
    print('Код валюты не введен, будут показаны значения по умолчанию')
    print(currency_rates('USD'))
    print(currency_rates('Eur'))
    print(currency_rates('jpy'))
    print(currency_rates('GBp'))
    print(currency_rates('RUB'))


# Результаты запуска в терминале PyCharm:
# (pythonProject5) python dz_4_5.py gbp
# (91.9773, [datetime.date(2022, 4, 28)])
# (pythonProject5) python dz_4_5.py usd
# (72.8764, [datetime.date(2022, 4, 28)])
# (pythonProject5) python dz_4_5.py jpy
# (57.1042, [datetime.date(2022, 4, 28)])
