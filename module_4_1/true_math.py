from math import inf # из модуля math импортирует бесконечность

def divide(first, second): # создание функции
    if second != 0: # проверка условия
        f = first/second # деление
        return f # возврат результата
    else:
        return inf # возврат бесконечность