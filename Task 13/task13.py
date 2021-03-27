print('Фильтр')

str_array = []
for i in range(int(input('Введите количество строк: '))):
    string = input()
    if string[:2] == '%%':
        string = string[2:]
        str_array.append(string)
    elif string[:4] == '####':
        string = ''
    else:
        str_array.append(string)
for i in str_array:
    print(i)