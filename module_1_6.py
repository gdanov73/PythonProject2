my_dict={"Aleks":1972,"Sergei":1973,"Val":1949,"Leonid":1958,"Nina":1926,"Ivan":1924} # создание ловаря
print("Dict:",my_dict) # вывод на экран списка знакомых с годом рожд.
print("Г.р. ",my_dict["Nina"]) # вывод года рожд.(значения) по имени(ключу)
print("Нет в списке",my_dict.get("Valera")) # задаем несуществующий ключ

my_dict.update({"Anna":1997,"Sandra":2000}) # добавляем еще данные 2-х человек
print(my_dict.pop("Ivan")) # удаляем одно имя

print("Обновленный список:",my_dict) # печатаем обновленный список



my_set={1,'ball',10,1917,'cub',3.14,1,'ball',10} # создаем множ-во
print(my_set) # выводим множ-во на экран
my_set.add('string')
my_set.add('cosmos') # добавляем 2 элемента
my_set.remove("ball") # удаляем 1 элемент
print(my_set)



