class House: # создание класса House
    def __init__(self, name, number_of_floors): # создание метода __init__
        self.name = name # имя ЖК
        self.number_of_floors = number_of_floors # кол-во этажей

    def go_to(self, new_floor): # метод go_to
        if 1 < new_floor < self.number_of_floors: #  проверка условия
            for i in range(1, new_floor + 1):
                print(i) # вывод на экран результата
            else:
                print('Такого этажа не существует') # -//-//-

    def __len__(self):
        return self.number_of_floors #   метод возвращает кол-во этажей
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.' # метод возвращает строку с данными класса

    def __eq__(self, other): # метод сравнения на равенство объектов класса House
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return False

    def __lt__(self, other): # метод сравнения на "меньше"
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return NotImplemented

    def __le__(self, other): # метод сравнения "меньше или равно"
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return NotImplemented

    def __gt__(self, other): # метод сравнения "больше чем"
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return NotImplemented

    def __ge__(self, other): # метод сравнения "больше или равно"
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return NotImplemented

    def __ne__(self, other): # метод сравнения на неравенство
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return True

    def __add__(self, value): # метод добавления элемента
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        elif isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        else:
            return NotImplemented

    def __radd__(self, value): # метод симметричного сложения
        return self.__add__(value)

    def __iadd__(self, value): # метод сложения с присваиванием
        return self.__add__(value)

h1 = House('ЖК Эльбрус', 10) # создаем элемент класса House
h2 = House('ЖК Акация', 20) # -//-//-

print(h1) # выод на экран результатов
print(h2) # -//-//

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)



























h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__


