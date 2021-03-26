print('Розенкранц и Гильденстерн меняют профессию')

string  = input('Введите о - если орел, р - решка: ')
count = 1
max = 0
for i in string:
    if i == 'о':
        count += 1
        max = count
    elif i == 'р':
        max = count
        count = 0
    else:
        exit(0)
print(max)