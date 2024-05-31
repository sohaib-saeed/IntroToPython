def Capitalization(s):
    if ord(s[0]) > 96:
        capital = ord(s[0]) - 32
        print(chr(capital) + s[1::])
    else:
        print(s)
s = str(input())
Capitalization(s)