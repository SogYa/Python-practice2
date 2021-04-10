print('Перестраиваемся в очередь')

num = int(input())
queue = []
for _ in range(num):
    string = input().split()
    if 'встал' in string[1]:
        queue.append(string[0])
    elif string[0] == 'Привет,':
        queue.insert(queue.index(string[1][:-1]) + 1, string[2])
    elif string[1] == 'хватит':
        queue.remove(string[0][:-1])
print(*queue, sep='\n')