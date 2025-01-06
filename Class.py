grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]] # список оценок
students = {'Johnny', 'Bilbo', 'Steve', 'Hendrik', 'Aaron'} # список студентов
students = list(students) # замена мн на список
students.sort() # выстраивание имен по алфавиту
print(students) # вывод имен на экран
journal = {} # оздание словаря
journal[students[0]]=sum(grades[0])/len(grades[0]) # вычисление  среднего балла
journal[students[1]]=sum(grades[1])/len(grades[1]) # -/-/-
journal[students[2]]=sum(grades[2])/len(grades[2]) # -/-/-
journal[students[3]]=sum(grades[3])/len(grades[3]) # -/-/-
journal[students[4]]=sum(grades[4])/len(grades[4]) # -/-/-
print(journal) # вывод среднего балла каждого студента на экран


