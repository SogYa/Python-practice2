print('Периодическая дробь')

num = int(input('Введите число: '))
first_pos = {}
position = 0
period = ""
remainder = 1

while not remainder in first_pos:
    first_pos[remainder] = position
    period += str(remainder // num)
    remainder = (remainder % num) * 10
    position += 1

period = period[first_pos[remainder]:]

print(period)