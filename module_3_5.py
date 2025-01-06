def get_multiplied_digits(number): # создание функции
    str_number = str(number) # преобразование числа в строку
    if len(str_number) > 1: # проверка условия
        first = int(str_number[0]) # выделяем первую цифру    30
        return first * get_multiplied_digits(int(str_number[1:])) # вызов функции
    else:
        if number == 0 :
            return 1
        return int(str_number) # возврат результата функции

result1 = get_multiplied_digits(40203) # вычисление произведения
print(result1) # печать результата
result2 = get_multiplied_digits(402030) # вычисление произведения
print(result2) # печать результата




