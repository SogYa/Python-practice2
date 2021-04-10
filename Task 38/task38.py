print('Длинношееед')

string = input('введите строку: ')
string = string.upper()
num = 0
for i in range(len(string)):
    if string.count(string[i]) > num:
        num = string.count(string[i])
print(num)