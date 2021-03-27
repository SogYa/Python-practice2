print('RLE')

string = input('Введите число: ')
count = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            count += 1
        else:
            a = string[i]
            print(count, string[i])
            cout = 1
print(count, string[i])