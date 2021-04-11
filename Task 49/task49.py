print('Права доступа')

ways = ["/home/ivan/Documents", "/var/www", "/home/alex"]
files = ["/home/alex/HarryPotter8.doc", "/home/ivan_urgant/game.exe", "/www/index.html"]

lst_ways = [x.split('/')[1:] for x in ways]
lst_files = [x.split('/')[1:] for x in files]


def check_permissions(ways, file):
    for x in ways:
        if len(file) < len(x):
            continue
        else:
            if x == file[:len(x)]:
                return 'YES'
    return 'NO'


print(check_permissions(lst_ways, lst_files[0]))
print(check_permissions(lst_ways, lst_files[1]))
print(check_permissions(lst_ways, lst_files[2]))