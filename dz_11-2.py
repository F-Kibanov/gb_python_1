"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
    вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
    завершиться с ошибкой.
"""


class MyEx:
    def __init__(self, message='Zero division is prohibited!'):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def check(num, div):
        try:
            if div == 0:
                raise ZeroDivisionError()
            else:
                return num / div
        except ZeroDivisionError as e:
            print(f'Zero division is not allowed {e}')


a = MyEx.check(1, 0)
print(a)
