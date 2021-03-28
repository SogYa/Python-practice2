print('Сортировка в обратном порядке')

nums_array = []
for i in range(int(input('Введите количество чисел: '))):
    nums_array.append(int(input('Введите число: ')))
nums_array.sort()
nums_array.reverse()
for i in nums_array:
    print(i)
