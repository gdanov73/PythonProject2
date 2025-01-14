def single_root_words(root_word, *other_words) : # задание функции
    same_words = [] # создание пустого списка
    for i in other_words : # начало цикла
        if root_word.lower() in i.lower() or i.lower() in root_word.lower() : # проверка вхождения слов друг в друга
            same_words.append(i) # заполнение списка
    return same_words # возврат заполненного списка






result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies') #  оздание списка 1

result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel') # создание пика 2

print(result1) # вывод на консоль списка 1

print(result2) # вывод на консоль списка 2


