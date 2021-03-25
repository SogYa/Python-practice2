print('Новые блюда')

dishes = set()
day_dishes = set()
for i in range(int(input('Количество блюд: '))):
    dishes.add(input('Блюдо: '))
for i in range(int(input('Количество дней: '))):
    name_of_recipe = ' '
    for j in range(int(input('Количество блюд: '))):
        day_dishes.add(input('Название блюда: '))
not_appearing_dishes = dishes - day_dishes
if len(not_appearing_dishes) > 0:
    for i in not_appearing_dishes:
        print('Блюдо, которое ниразу не готовилось:',i)
else:
    print('Все блюда были приготовлены')