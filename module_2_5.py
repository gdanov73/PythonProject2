def get_matrix(n,m,value): # создаем функцию
    matrix = [] # создание пустого списка
    for i in range(1,n+1) : # начало цикла, строки
        sublist = [] # создание пустого подсписка
        for a in range(1,m+1) : # внутренний цикл, столбцы
            sublist.append(value) # добавления элемента в подсписок
        matrix.append(sublist) # добавление подсписка в список
    return matrix # возврат значения функции

result1 = get_matrix(2, 2, 10) # ввод данных

result2 = get_matrix(3, 5, 42) # -//-//-

result3 = get_matrix(4, 2, 13) # -//-//-

print(result1) # вывод на экран результата

print(result2) # -//-//-

print(result3) # -//-//-