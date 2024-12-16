def print_params(a=1, b="строка", c=True) : # создание функции
    print(a, b,  c) # вывод параметров на консоль

print_params() # вызов функции без параметров
print_params(a=0.1, b=False, c={'Alex': 24}) # вызов функции с заменой параметров
print_params(b=25) #  вызов функции с другим b
print_params(c=[1,2,3]) # вызов функции с другим c
values_list=('Peter', True, 3.14) # создание списка
values_dict={'a':200, 'b':400, 'c':True} # создание словаря
print_params(*values_list) # вызов функции с переданным списком
print_params(**values_dict) # вызов функции с переданным словарем

values_list_2 = [54.32, 'Строка' ] # создание второго списка

print_params(*values_list_2, 42) # проверка работы функции с этим списком