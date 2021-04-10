print('csv 2.0')

all = []
for i in range(int(input())):
    string = input().split(',')
    all.append(string)
for i in range(int(input())):
    cords = [int(i) for i in input().split(',')]
    d = all[cords[0]]
    word = d[cords[1]]
    print(word)