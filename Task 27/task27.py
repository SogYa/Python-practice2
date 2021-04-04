print('Два пути')

num = int(input())
first = [int(input()) for i in range(num)]
second = first[:]
training = int(input())
for i in range(training):
    brother = int(input())
    if brother == 1:
        first[int(input())] += int(input())
    elif brother == 2:
        second[int(input())] += int(input())
print(*first)
print(*second)
dd = 0
for i in range(len(first)):
    if first[i] == second[i]:
        dd = dd + 1
print(dd)