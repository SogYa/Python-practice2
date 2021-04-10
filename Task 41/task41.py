s = [0 for i in range(30001)]
pos = 0
string = input()

i = 0
while (i < len(string)):
    if string[i] == ">":
        pos = pos + 1
    elif string[i] == "<":
        pos = pos - 1
    elif string[i] == ".":
        print(s[pos])
    elif string[i] == "+":
        s[pos] = s[pos] + 1
        if s[pos] > 255:
            s[pos] = 0
    elif string[i] == "-":
        s[pos] = s[pos] - 1
        if s[pos] < 0:
            s[pos] = 255
    elif string[i] == '[':
        if s[pos] == 0:
            j = i + 1
            c = 1
            while (True):
                if string[j] == '[':
                    c += 1
                if string[j] == ']':
                    c -= 1
                if c == 0:
                    i = j
                    break
                j += 1
    elif string[i] == ']':
        c = -1
        j = i - 1
        while (True):
            if string[j] == ']':
                c -= 1
            if string[j] == '[':
                c += 1
            if c == 0:
                i = j - 1
                break
            j -= 1

    i += 1