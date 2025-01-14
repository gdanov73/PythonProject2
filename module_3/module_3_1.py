calls=0 # переменная(кол-во вызовов функций)
def count_calls() : # Функция count_calls подсчитывающая вызовы остальных функций.
    global calls # объявление переменной calls глобальной
    calls = calls + 1 # суммируется с кл-вом предыдущих вызовов
def string_info(string:str) : # принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    len(string) # подсчет кол-ва символов в строке
    string.upper() # перевод в верхний регистр
    string.lower() # перевод в нижний регистр
    b = (len(string), string.upper(), string.lower()) # создание кортежа
    count_calls() # подчет вызовов функций
    return b # возвращение кортежа
def is_contains(string: str,list_to_search: list) : # принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует.
    count_calls() # подсчет вызовов фукции
    for i in list_to_search : # перебор элементов в списке
        if string.lower() == i.lower() : # проверка условия(совпадает ли строка с элементом в списке
           return  True # возвращение значения функции
    return False # -//-//-
print(string_info('Capybara')) # ввод данных
print(string_info('Armageddon')) # ввод данных
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN #
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches #
print(calls) # печать кол-ва вызовов функций
