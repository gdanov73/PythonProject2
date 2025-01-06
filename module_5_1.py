class House: # создание класса House
    def __init__(self, name, number_of_floors): # конструктор класса
        self.name = name # Создание атрибута name
        self.number_of_floors = number_of_floors # создание атрибута number_of_floors
    def go_to(self, new_floor): # метод
        if 0 < new_floor <= self.number_of_floors: # проверка что этаж есть в данном доме
            for floor in range(1, new_floor + 1): # цикл от 1 этажа до указанного
                print(floor) # вывод  на экран номера этажа
        else:
            print('Такого этажа не существует') # Иначе вывод фразы

h1 = House('ЖК Горский', 18) # создание экземляра класса
h2 = House('Домик в деревне', 2) # создание 2 экземпляра класса
h1.go_to(5) # вызов метода
h2.go_to(10) # вызов метода
