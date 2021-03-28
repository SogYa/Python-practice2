print('Наперстки')

num = int(input('Введите количество наперстков: '))
list = ['']*num
for i in range(num):
    list[i] = input('Введите что находится под наперстком: ')
cout = int(input('Количество перестановок: '))
for i in range(cout):
    swap = int(input())
    tmp = ['']*swap
    for j in range(swap):
        tmp[j] = list[int(input())-1]
    list = tmp
for i in range(len(list)):
    print(list[i])