"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
    В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год
    и преобразовывать их тип к типу «Число».
    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
    Проверить работу полученной структуры на реальных данных.
"""


class MyDate:
    def __init__(self, string):
        self.date = string

    @classmethod
    def date_to_int(cls, obj):
        my_date = obj.date.split('-')
        for d in my_date:
            print(int_d := int(d))
            print(type(int_d))

    @staticmethod
    def check_date(obj):
        my_date = obj.date.split('-')
        day, month, year = my_date
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            if 0 < day < 32 and 0 < month < 13:
                return day, month, year
            raise ValueError('Invalid date')
        except ValueError as e:
            print(f'Incorrect date: {e}')
        except TypeError as e:
            print(f'Incorrect date: {e}')


a = MyDate('12-01-1990')
print(MyDate.date_to_int(a))

b = MyDate('42-01-1990')
print(MyDate.check_date(b))
