class House: # создание класса House
    def __init__(self, name, number_of_floors): # создание метода __init__
        self.name = name # название ЖК
        self.number_of_floors = number_of_floors # кол-во этажей

    def go_to(self, new_floor): # метод go_to
        if 1 < new_floor < self.number_of_floors: # проверка условия
            for i in range(1, new_floor + 1): # цикл
                print(i) # вывод на экран результата
            else:
                print('Такого этажа не существует') # -//-//-

    def __len__(self): # метод возвращает кол-во этажей
        return self.number_of_floors

    def __str__(self): # метод возвращает строку с данными класса
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other): # метод сравнения на равенство объектов класса House
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other): # метод сравнения на "меньше"
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other): # метод сравнения "меньше или равно"
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other): # метод сравнения "больше чем"
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other): # метод сравнения "больше или равно"
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other): # метод сравнения на неравенство
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value): # метод добавления элемента
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value): # метод симметричного сложения
        self.number_of_floors += value
        return self

    def __iadd__(self, value): # метод сложения с присваиванием
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    houses_history = [] # создание атрибута houses_history

    def __new__(cls, *args): # метод __new__ вызывается перед методом  __init__
        cls.houses_history.append(args[0]) # добавляем объект в атрибут houses_history
        return object.__new__(cls)

    def __del__(self): # вывод сообщения об удалении объекта
        print(f'{self.name} снесен, но он останется в истории')


h1 = House('ЖК Эльбрус', 10) # создание объекта h1
print(House.houses_history) # вывод на экран
h2 = House('ЖК Акация', 20)  # -//-//-  h2
print(House.houses_history) # -//-//-
h3 = House('ЖК Матрёшки', 20) #  -//-//-  h3
print(House.houses_history) # -//-//-

del h2 # удаление объектов
del h3 #-//-//-

print(House.houses_history) # печать истории существующих объектов