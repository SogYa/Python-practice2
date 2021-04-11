print('Дни рождения 2')

Birthday = {'янв': [], 'фев': [], 'мар': [], 'апр': [], 'май': [],
        'июн': [],'июл': [],'авг': [],'сен': [],'окт': [],
        'ноя': [],'дек': [], }
for i in range(int(input('Введите количество человек: '))):
    about = input('Имя, день рождения, месяц: ').split()
    name = about[0]
    month = about[2]
    Birthday[month].append(name)
    Birthday[month].sort()
for j in range(int(input('Количество человек в поиске: '))):
    inputm = input('Введите месяц: ')
    print(' '.join(Birthday[inputm]))
