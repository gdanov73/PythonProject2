class Vehicle :
    owner(str)
    __model(str)
    __engine_power(int)
    __color(str)
    def  get_model :
        pass
    def  get_horsepower :
        pass
    def get_color :
        pass
    def print_info :
        pass
    def set_color
        pass
class Sedan :
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



