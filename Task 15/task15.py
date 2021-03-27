print('Минификатор')

n = int(input())
mark = False
slash = False

char = 0
result = []

for i in range(n):
    string = input()
    while string[char] == " ":
        result.append(" ")
        char += 1
    for i2 in range(char, len(string)):
        if not slash:
            if string[i2] == "'":
                result.append(string[i2])
                mark = not mark
            elif string[i2] == "\\":
                result.append(string[i2])
                slash = True
            elif string[i2] == "#":
                if mark:
                    result.append(string[i2])
                else:
                    break
            elif string[i2] == " ":
                if mark:
                    result.append(string[i2])
                else:
                    if i2 + 1 != len(string):
                        if string[i2 + 1] == " ":
                            result.append("")
                        else:
                            result.append(string[i2])
            else:
                result.append(string[i2])
        else:
            slash = False
            result.append(string[i2])
    print("".join(result))
    result = []
    mark = False
    slash = False
    char = 0