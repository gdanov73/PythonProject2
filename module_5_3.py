#  1. Создаем класс House.
class House:
    #  2. Внутри класса House определяем метод __init__, в который передадаем название и кол-во этажей.
    def __init__(self, name, number_of_floors):
        #  3. Внутри метода __init__ создаем атрибуты объекта self.name и self.number_of_floors,
        #  присваиваем им переданные значения.
        self.name = name
        self.number_of_floors = number_of_floors

    #  4. Создаем метод go_to с параметром new_floor и записываем логику внутри него на основе описания задачи 5_1.
    def go_to(self, new_floor):
        #  Если же new_floor больше чем self.number_of_floors или меньше 1,
        #  то вывести строку "Такого этажа не существует".
        if 1 < new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors #  в методе возвращает кол-во этажей
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

    # 2.5. Методом сравнения на неравенство
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