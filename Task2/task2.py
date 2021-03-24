print('Посещаемость')

num_of_lists = int(input('Количество списков: '))
num_of_students = 0
counter = 0
list_array = []

for i in range(num_of_lists):
    num_of_students = int(input('Количество фамилий в списке: '))
    students_set = set()
    for j in range(num_of_students):
        students_set.add(input('Введите имя ученика: '))
    list_array.append(students_set)
print(list_array)
for j in list_array: