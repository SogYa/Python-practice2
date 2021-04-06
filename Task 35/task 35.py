import re
print('GET')


t = input('Введите URL: ')
key = input('Введите ключ: ')
print(re.search(f'\?.*?{key}=(.*)[&\n]', t)[1])