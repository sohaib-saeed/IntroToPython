def CanSum(s):
    string = []
    if len(s) > 1:
        for i in range(len(s)):
            if s[i] != "+":
                string.append(s[i])
        for i in range(len(string)):
            for j in range(i+1,len(string)):
                if int(string[i]) > int(string[j]):
                    string[i],string[j] = string[j],string[i]
        for i in range(len(string)-1):
            print(string[i],end="+")
        print(string[-1])
    else:
        print(s)
s = str(input())
CanSum(s)
