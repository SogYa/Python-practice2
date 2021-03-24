print('Рецепты')

products = set()
products_of_recipe = set()
for i in range(int(input('Количество продуктов в холодтльнике: '))):
    products.add(input('Продукт: '))
for i in range(int(input('Количество рецептов: '))):
    bool = False
    name_of_recipe = input('Название рецепта: ')
    for j in range(int(input('Количество продуктов в рецепте: '))):
        products_of_recipe.add(input('Ингредиент: '))
    for i in products_of_recipe:
        if i in products:
            bool = True
    if bool:
        print(name_of_recipe)
    products_of_recipe = set()
