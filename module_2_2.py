print("Введите 3 числа:") # начало программы
first=int(input()) # ввод 1-го числа
second=int(input()) # ввод 2-го числа
third=int(input()) # ввод 3-го числа
if first==second and second==third: # проверка условия, когда все числа равны между собой
 print("3") #  вывод на экран результата
elif first==second or first==third or second==third or first==third: # рпроверка равенства какой-либо пары между собой
    print("2") # вывод результата на экран
else:print("0") # вывод на экран результата, когда все числа разные


