print('Вертикальная диаграмма')

string = input('Введите числа через пробел: ')
string_split = string.split()
len_string_split = len(string_split)
for _ in range(len_string_split+3):

    print("*" * (len_string_split+2))