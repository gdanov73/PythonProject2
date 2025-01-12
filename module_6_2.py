class Vehicle : # создание класса Vehicle
    __COLOR_VARIANTS = ["red", "blue","green", "black", "white"] # создание списка цветов машины
    def __init__(self, owner, model, color, engine_power ): # конструктор класса
       self.owner = owner # присвоение значения атрибуту
       self.__model = model # -//-//-
       self.__engine_power = engine_power # -//-//-
       self.__color = color # -//-//-
    def  get_model(self): #  получение строки с названием модели
        return "Модель:" + self.__model #  возврат строки

    def  get_horsepower(self): # получение строки с мощностью двигателя
        return "Мощность двигателя:" + str(self.__engine_power) # возврат строки

    def get_color(self): # получение строки с цветом машины
        return "Цвет:" + self.__color # возврат строко

    def print_info(self): # печать информации
        print(self.get_model()) # модель
        print(self.get_horsepower()) # мощность
        print(self.get_color()) # цвет
        print(" Владелец: ", self.owner) # владелец
    def set_color(self, new_color:str): # установка цвета машины
        if new_color.lower() in self.__COLOR_VARIANTS: # если цвет машины из списка
            self.__color = new_color # то цвет меняют на новый
        else: # иначе
            print("Нельзя сменить цвен на новый " + new_color) # печать невозможности мены цвета
class Sedan(Vehicle) : # создание класса  Sedan
    __PASSENGERS_LIMIT = 5 # кол-во мест



    # Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()



