print('A272727')

array = [0]
num = int(input('Введите количество чисел: '))
for i in range(num):
    b = 0
    for j in range(len(array)):
        if array[j] == array[-1 - j]:
             b += 1
    array.append(b)
del array[-1]
for i in array:
    print(i)