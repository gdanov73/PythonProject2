class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self, new_floor):
        if 1 < new_floor < self.number_of_floors:
            for i in range(1, new_floor + 1):
                print(i)
            else:
                print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors # в методе возвращает кол-во этажей
    def __str__(self):
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}" # метод возвращает строку с данными класса

h1 = House('ЖК Эльбрус', 10) # создаем элемент класса House
h2 = House('ЖК Акация', 20) # -//-//-

print(h1) # вывод на экран данных h1
print(h2) # -//-//- h2
print(len(h1)) # вывод на экран кол-ва зтажей h1
print(len(h2)) # -//-//- h2 