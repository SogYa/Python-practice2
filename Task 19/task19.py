print('Подробный список покупок')

shopping_list = []
for i in range(int(input('Количество позиций: '))):
    string = input('Наименование товара: ') + ' ' +input('Количество: ')
    shopping_list.append(string)
shopping_list.reverse()
for i in shopping_list:
    print(i)
