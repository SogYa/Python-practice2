print('Цезарь его знает')

alphabet = 'абвгдеёжзиклмнопрстуфхцчшщъыьэюя'
num = int(input('Введите ключ: '))
string = input('Введите сообщение: ')
cipher = ' '
for i in string:
    if ord(i) >= 1101:
        i = chr(ord(i) - (32 - num))
    else:
        i = chr(ord(i) + num)
    cipher += i
print(cipher.lstrip())
