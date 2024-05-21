grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a=list(students)#переводим множество в список
list.sort(a)#сортируем список по алфавиту
#print(a)#Проверяем
Aaron_grade=sum(grades[0])/len(grades[0])#Находим средний балл для каждого ученика
Bilbo_grade=sum(grades[1])/len(grades[1])
Johnny_grade=sum(grades[2])/len(grades[2])
Khendrik_grade=sum(grades[3])/len(grades[3])
Steve_grade=sum(grades[4])/len(grades[4])
#print(Aaron_grade)#Проверяем
Journal={}#Создаем словарь
Journal[a[0]]=Aaron_grade#Добавляем ключ и значение
Journal.update({a[1]:Bilbo_grade,a[2]:Johnny_grade,a[3]:Khendrik_grade,a[4]:Steve_grade})#Обновляем словарь
print(Journal)
