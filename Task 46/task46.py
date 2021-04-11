print('Телефонная книга')

dict = {}
for i in range(int(input('Количество записей: '))):
    value, key = input('Номер и имя: ').split()
    if key in dict:
        dict[key].append(value)
    else:
        dict[key] = [value]

for i in range(int(input('Номер записи: '))):
    key = input('Имя: ')
    if key in dict:
        print(*dict[key])
    else:
        print('Нет в телефонной книге')
