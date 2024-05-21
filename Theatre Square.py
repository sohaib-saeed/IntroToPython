import math
def TheatreSquare(n,m,a):
    return math.ceil(n / a) * math.ceil(m / a)
n,m,a = input().split()
n = int(n)
m = int(m)
a = int(a)
print(TheatreSquare(n,m,a))