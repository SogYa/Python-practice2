print('Продолжайте говорить "А"')

string = input('Введите строку: ')
while string[0] == 'а' or string[0] == 'А':
    string = input('Введите строку: ')
else:
    exit(0)