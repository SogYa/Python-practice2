print('Тотальная дециммация')

num_of_soldiers = int(input('Введите количество солдат: '))
soldiers = []
for i in range(num_of_soldiers):
    soldiers.append(input('Введите имя солдата: '))
k = int(input())
n = 0
print(soldiers[0])
del soldiers[0]
for i in range(num_of_soldiers):
    if len(soldiers) > n + k - 1:
        n += k - 1
        print(soldiers[n])
        del soldiers[n]
    else:
        n = 0
        if len(soldiers) > n:
            print(soldiers[n])
            del soldiers[n]