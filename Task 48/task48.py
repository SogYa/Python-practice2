print('Репосты')

num = int(input())
string = input()
time = 0
public, like = string.split(' опубликовал пост, количество просмотров: ')
d = {public: [int(like), 'root', time]}
for i in range(1, num):
    string = input()
    time += 1
    if ' отрепостил пост у ' in string:
        repost, string = string.split(' отрепостил пост у ')

        if ', количество просмотров: ' in string:
            autor, like = string.split(', количество просмотров: ')
            like = int(like)
            d[repost] = [like, autor, time]
            while autor != 'root':
                d[autor][0] += like
                autor = d[autor][1]
    elif 'количество просмотров: ' in string:
        string, like = string.split('количество просмотров: ')
        d[public][0] += int(like)
for x in sorted(d, key=lambda y: d[y][2]):
    print(d[x][0])