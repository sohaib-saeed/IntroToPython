def compare_strings(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    else:
        return 0

string1 = input().strip()
string2 = input().strip()
print(compare_strings(string1, string2))
