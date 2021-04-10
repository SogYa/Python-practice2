print('Знаков без пробелов')


string = input('Введите строку: ')
string_split = string.split(' ')
counter = 0
for i in string_split:
    for j in range(len(string_split)):
        counter += 1
print(counter)