immutable_var=2000, False, "Аня" # создание кортежа с элементами разных типов данных
print("Immutable tuple:")
print(immutable_var) #  вывод кортежа на экран

immutable_var[0]=20 # попытка замены первого элемента кортежа
print(immutable_var)

mutable_list=(["ананас", "груша" , "перcик ","виноград"]) # создание спика из нескольких элементов
mutable_list[1]="2" # замена 2-го элемента на цифру 2
mutable_list[2]="3" # замена 3-го элемента на цифру 3
print("Mutable list:")
print(mutable_list ,"Modified") # вывод на экран обновленного списка