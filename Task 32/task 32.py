print('etc/passwd')

a = []
b = list(input().split(':'))
while b != ['']:
    a.append(b)
    b = list(input().split(':'))
c = list(input().split(';'))
for i in range(len(a)):
    if c.count(a[i][1]) != 0:
        print('To:', a[i][0])
        m = a[i][4].split(',')
        print(m[0] + ',' + ' ваш пароль слишком простой, смените его.')