calls=0 # переменная(кол-во вызовов функций)
def count_calls() : # Функция count_calls подсчитывающая вызовы остальных функций.
    global calls # превращение переменной в глобальную
    calls = calls + 1 # суммируется с кл-вом предыдущих вызовов
def string_info(string:str) : # принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    len(string) # подсчет кол-ва имволов в строке
    string.upper() # верхний регистр
    string.lower() # нижний регистр
    b = (len(string), string.upper(), string.lower()) # кортеж
    count_calls() # подчет вызовов
    return b #
def is_contains(string: str,list_to_search: list) : # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.
    count_calls() #
    for i in list_to_search : # начало цикла
        if string.lower() == i.lower() : # выполнение условия
           return  True #
    return False #
print(string_info('Capybara')) # ввод данных
print(string_info('Armageddon')) # ввод данных
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN #
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches #
print(calls) # печать кол-ва вызовов функций
