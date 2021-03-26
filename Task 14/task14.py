print('Именна та буква')

string = input('введите слово: ')
lovely_num = int(input('введите любимое число Аркадия: '))
lovely_char = input('Введите любимую букву Аркадия: ')
try:
    if string[lovely_num-1] == lovely_char:
        print('ДА')
    elif len(lovely_char) > 1 or (1 > lovely_num > len(lovely_char)):
        print('ОШИБКА')
    else:
        print('НЕТ')
except IndexError:
    print('ОШИБКА')

