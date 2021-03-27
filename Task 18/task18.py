print('Проверка чека')

s = input()
n, total = int(s[:4]), int(s[4:])
errors, true_total = [], 0
for i in range(n):
    s = input()
    price, amount, cost = int(s[:7]), int(s[8:12]), int(s[13:])
    if price * amount != cost:
        errors.append(i+1)
    true_total += cost
print(total - true_total)
for x in errors:
    print(x, end=' ')