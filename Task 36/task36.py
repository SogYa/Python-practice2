print('Гедсби')

char = input('Введите символ: ')
chr1 = char.upper()
string = input('Введите строку: ')
string_split = string.split(' ')
for i in string_split:
    if char in i or chr1 in i:
        print(i)