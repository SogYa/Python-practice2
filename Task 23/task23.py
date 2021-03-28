print('Масшатбирование')

num_of_string = int(input('Введите количество строк: '))
num_of_column = int(input('Введите количество столбцов: '))
list = []
for i in range(num_of_string):
    list.append(input())
list2=[]
for i in list[::2]:
    list2.append(i[::2])
num_of_string = num_of_string // 2
num_of_column = num_of_column // 2
for i in list2:
    print(i)