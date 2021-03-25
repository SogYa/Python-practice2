print('Какая-то там буква')

string = input('Введите сообщение: ')
index = int(input('Натуральное число: '))
if index > 0 and index <= len(string):
    print(string[index-1])
else:
    print('ОШИБКА')
    exit(0)