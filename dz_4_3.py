from requests import get, utils
import re
from datetime import date
# import decimal                                           # Раскомментировать для использования формата  decimal


def currency_rates(code: str) -> tuple:
    """возвращает курс валюты `code` по отношению к рублю"""

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    currency_str = response.content.decode(encoding=encodings).replace(",", ".")
    cur_date = currency_str.find('Date')
    cur_date = currency_str[cur_date + 6: cur_date + 16]
    currency_date = [date.fromisoformat(f'{cur_date[6:]}-{cur_date[3:5]}-{cur_date[:2]}')]

    dict_key = (' '.join(re.findall(r'<CharCode>([^<>]+)</CharCode', currency_str))).split()
    dict_val = (' '.join(re.findall(r'<Value>([^<>]+)</Value>', currency_str))).split()
    currency_dict = dict(zip(dict_key, dict_val))
    try:
        code = code.upper()
        result_value = float(currency_dict.get(code))
        # result_value = decimal.Decimal(result_value)              # При раскомментировании значение курса будет
        # print(type(result_value))                                 # выводится в формате decimal
        return result_value, currency_date
    except TypeError:
        return None, currency_date

# result_value = 1.11  ## здесь должно оказаться результирующее значение float


print(currency_rates("usd"))
print(currency_rates("EUR"))
print(currency_rates("noname"))
