from collections import Counter

print('Посещаемость')

students_array = []
num_of_lists = int(input('Количество списков: '))
for i in range(num_of_lists):
    num_of_students = int(input('Количество фамилий в списке: '))
    for j in range(num_of_students):
        students_array.append(input('Введите имя ученика: '))
dictionary =dict(Counter(students_array))
for element in dictionary:
    if dictionary.get(element) == num_of_lists:
        print(element)