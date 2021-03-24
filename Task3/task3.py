print('Однофамильцы')
men_set = []
res = 0
for i in range(int(input('Количество мужчин-сотрудников: '))):
    men_set.append(input('Фамилия сотрудника: '))
for j in set(men_set):
    counter = 0
    for men in men_set:
        if men == j:
            counter += 1
    if counter > 1:
        res += counter
print('Количество однофамильцев',res)