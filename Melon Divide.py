def MelonDivide(weight):
        if weight > 2 and weight % 2 == 0:
            return "YES"
        else:
            return "NO"

weight = int(input())
print(MelonDivide(weight))



