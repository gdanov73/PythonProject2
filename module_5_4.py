class House: #
    def __init__(self, name, number_of_floors):
        self.name = name #
        self.number_of_floors = number_of_floors #

    def go_to(self, new_floor): #
        if 1 < new_floor < self.number_of_floors: #
            for i in range(1, new_floor + 1): #
                print(i) #
            else:
                print('Такого этажа не существует') #

    def __len__(self): #
        return self.number_of_floors

    def __str__(self): #
        return f"Название: {self.name}, количество этажей: {self.number_of_floors}"

    def __eq__(self, other): #
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other): #
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other): #
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other): #
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other): #
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other): #
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value): #
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value): #
        self.number_of_floors += value
        return self

    def __iadd__(self, value): #
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    houses_history = [] #

    def __new__(cls, *args): #
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors): #
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self): #
        print(f'{self.name} снесен, но он останется в истории')


h1 = House('ЖК Эльбрус', 10) #
print(House.houses_history) #
h2 = House('ЖК Акация', 20)  #
print(House.houses_history) #
h3 = House('ЖК Матрёшки', 20) #
print(House.houses_history) #

del h2 # удаление объектов
del h3 #-//-//-

print(House.houses_history) #