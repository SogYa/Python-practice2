print('Парадоксы статистики')

med = []
mod = []
all = []
for j in range(int(input())):
    s = list(map(int, input().split()))
    s.sort()
    z = s[len(s) // 2]
    mx = 0
    nxx = 0
    for i in s:
        if s.count(i) > mx:
            mx = s.count(i)
            nxx = i
    med.append(z)
    mod.append(nxx)
    for i in s:
        all.append(i)
all.sort()
print(*med)
print(*mod)
med.sort()
mod.sort()
print(med[len(med) // 2])
print(mod[len(mod) // 2])
print(all[len(all) // 2])
mx = 0
nxx = 1234
for i in all:
    if all.count(i) > mx:
        mx = all.count(i)
        nxx = i
print(nxx)