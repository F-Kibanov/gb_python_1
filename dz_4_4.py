from utils import currency_rates

print(currency_rates('usd'))
print(currency_rates('gbp'))
print(currency_rates('jpy'))
print(currency_rates('eur'))
print(currency_rates('aud'))
print(currency_rates('rub'))


# Результаты запуска в PyCharm:
# (72.8764, [datetime.date(2022, 4, 28)])
# (91.9773, [datetime.date(2022, 4, 28)])
# (57.1042, [datetime.date(2022, 4, 28)])
# (75.9224, [datetime.date(2022, 4, 28)])
# (52.318, [datetime.date(2022, 4, 28)])
# (None, [datetime.date(2022, 4, 28)])
