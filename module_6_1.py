class Plant: # создание класса Plant
    adible = False # съедобность
    def __init__(self, name): # конструктор класса
        self.name = name # присвоение значения атрибуту класса Plant

class Flower(Plant)  : # создание наследника Flower класса Plant
    pass #  выход из класса
class Fruit(Plant) : # создание наследника Fruit класса Plant
    adible = True # переопределение атрибута adible

class Animal: # создание класса Animal
    alive = True # живой, неживой
    fed = False # накормлен или нет
    def __init__(self, name): #  коструктор класса Animal
        self.name = name # присвоение значения атрибуту класса Animal
    def eat(self, food: Plant): # метод кормежка
        if food.adible == True : # проверка услоия на съедобность
            print(self.name+' съел '+food.name) # вывод на экран рез-та
            self.fed = True # животное накормлено
        else : # иначе
            print(self.name+" не стал есть "+food.name) # вывод на экран результата
            self.alive = False # животное умерло
class Mammal(Animal) : # создание класса травоядных
    pass #
class Predator(Animal) : # создание класса хищников
    pass #
# ввод данных задания
a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')


# вывод на экран рез-та
print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)
