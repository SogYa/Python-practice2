print('Крупные буквы')

a_array = ['    *    ','   * *   ','  *   *  ',' ******* ','*       *']
b_array = ['**** ','*   *','**** ','*   *','**** ']
c_array = ['****','*','*','*','****']

char = input('Введите ABC: ')
if len(char) == 3:
    if char == 'ABC':
        for i in range(5):
            print(a_array[i],' ',b_array[i],' ',c_array[i])
    else:
        print('Вы ввели не те буквы! ')
else:
    print('Вы ввели больше трех букв!')
    exit(0)