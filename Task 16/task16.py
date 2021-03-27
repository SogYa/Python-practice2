print('Буквоедство')

string = input('Введите слово: ')
while len(string) != 1:
    string = string[1:-1]
    print(string)