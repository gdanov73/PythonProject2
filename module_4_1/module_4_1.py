from module_4_1.fake_math import divide as fake_divide # импорт функции из fake_math
from module_4_1.true_math import divide as true_divide # импорт функции из true_m

result1 = fake_divide(69, 3) # первое вычисление
result2 = fake_divide(3, 0) # второе вычисление, показывает ошибку
result3 = true_divide(49, 7)# третье вычисление
result4 = true_divide(15, 0) # возврат бесконечность
print(result1) # печать результата
print(result2) # -//-//-
print(result3) # -//-//-
print(result4) # -//-//-
