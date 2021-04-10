print('Бактериям бой')

num = int(input())
bacteria = [[int(input()) for _ in range(num)] for _ in range(num)]
for _ in range(int(input())):
    x = int(input())
    y = int(input())
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                if bacteria[x + i][y + j] >= 8:
                    bacteria[x + i][y + j] -= 8
                else:
                    bacteria[x + i][y + j] = 0
            else:
                if (0 <= x + i <= num - 1) and (0 <= y + j <= num - 1):
                    if bacteria[x + i][y + j] >= 4:
                        bacteria[x + i][y + j] -= 4
                    else:
                        bacteria[x + i][y + j] = 0
for i in range(num):
    for j in range(num):
        print(bacteria[j][i], end=' ')
    print('')