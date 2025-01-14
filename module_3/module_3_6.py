def calculate_structure_sum(data): # создание функции
    total_sum = 0 # начальная сумма равна 0

    if isinstance(data, int): #
        total_sum += data # если элемент - число, добавляем его к сумме
    elif isinstance(data, str):
        total_sum += len(data) # если элемент - строка, добавляем её  к сумме
    elif isinstance(data, (list, tuple, set)):
        for item in data: # начало цикла
            total_sum += calculate_structure_sum(item) #  если элемент - список, кортеж или множество, рекурсивно обрабатываем каждый элемент
    elif isinstance(data, dict): # если элемент - словарь, рекурсивно обрабатываем ключи и значения
        for key, value in data.items(): # начало цикла
            total_sum += calculate_structure_sum(key) # добавление ключей к общей сумме
            total_sum += calculate_structure_sum(value) # добавление значений к общей сумме

    return total_sum # возврат суммы

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

