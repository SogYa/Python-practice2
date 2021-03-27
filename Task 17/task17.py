print('Белый список')

white_list = []
request_list = []
for i in range(int(input('Количество запросов в белом списке: '))):
    white_list.append(input('Запрос: '))
for i in range(int(input('Количество запросов на обработку: '))):
    request_list.append(input('Запрос: '))
for i in request_list:
    if i in white_list:
        print(i)