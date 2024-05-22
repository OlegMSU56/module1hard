students=sorted(list(students))
for A in range(len(grades)):
    grades[A]=sum(grades[A])/len(grades[A])
Journal={}#Создаем словарь
for i in range(len(students)):
    Journal[students[i]]=grades[i]
print(Journal)
