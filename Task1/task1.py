print('Книги на лето')

num_of_books1 = int(input('Количество книг на полке: '))
num_of_books2 = int(input('Количество книг в списке: '))
counter = 0
if num_of_books1 < 1 or num_of_books2 < 1:
    exit(0)
elif num_of_books2 > num_of_books1:
    exit(0)
books_array1 = [num_of_books1]
for i in range(num_of_books1):
    book = input('Введите название книги с полки: ')
    books_array1.append(book)
books_array2 = [num_of_books2]
for j in range(num_of_books2):
    book = input('Введите название книги из списка: ')
    for k in range(len(books_array1)):
        if book in books_array1:
            counter += 1
    if counter > 0:
        print('YES')
        counter = 0
    else:
        print('NO')