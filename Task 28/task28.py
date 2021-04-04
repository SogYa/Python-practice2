print('Финал и не финал')
kom_res = []
num_of_teams = int(input('Введите количество комманд: '))
for i in range(num_of_teams):
    kom_res.append((input(), int(input())))

    m = len(kom_res)
    for i in range(m - 1):
        for j in range(m - i - 1):
            if kom_res[j][1] > kom_res[j + 1][1]:
                kom_res[j], kom_res[j + 1] = kom_res[j + 1], kom_res[j]

    moiety = m // 2
    the_final = kom_res[moiety:]
    first = kom_res[: moiety]

    m = len(the_final)
    for i in range(m - 1):
        for j in range(m - i - 1):
            if the_final[j] > the_final[j + 1]:
                the_final[j], the_final[j + 1] = the_final[j + 1], the_final[j]

    for i in the_final:
        print(i[0])

    m = len(first)
    for i in range(m - 1):
        for j in range(m - i - 1):
            if first[j] > first[j + 1]:
                first[j], first[j + 1] = first[j + 1], first[j]

    for i in first:
        print(i[0])