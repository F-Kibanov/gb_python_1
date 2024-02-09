"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
    который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
    В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
    уникальные для каждого типа оргтехники.
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
