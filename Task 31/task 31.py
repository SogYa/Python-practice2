print('Только без лука')

recipe_string = ' '
recipe = []
num_of_strings = int(input('Введите количество строк в рецпете: '))
for i in range(num_of_strings):
    string = input('Введите  пункты ингридиент: ')
    if not 'лук' in string:
        if i != num_of_strings-1:
            recipe.append(string + ', ')
        else:
            recipe.append(string)
for i in recipe:
    recipe_string += i
print(recipe_string)