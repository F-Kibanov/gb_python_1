"""
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
    в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
    других данных, можно использовать любую подходящую структуру (например, словарь).
"""


class Warehouse:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.name, []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Equipment:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def __repr__(self):
        return f'{self.name} - {self.price} - {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, price, year):
        super().__init__(name, price, year)
        self.series = series

    def action(self):
        return f'Принтер {self} умеет печатать'


class Scanner(Equipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)

    def action(self):
        return f'Сканер {self} умеет сканировать'


class Xerox(Equipment):
    def __init__(self, name, price, year):
        super().__init__(name, price, year)

    def action(self):
        return f'Ксерокс {self} умеет копировать'


# Создаем переменную склада
wh = Warehouse()
# Добавляем оргтехнику на склад
scanner = Scanner('HP', '3000', 2020)
wh.add_to(scanner)
xerox = Xerox('Sony', '4000', 2019)
wh.add_to(xerox)
print(wh._dict)
# Убираем 'HP'
wh.extract('HP')
print(wh._dict)
