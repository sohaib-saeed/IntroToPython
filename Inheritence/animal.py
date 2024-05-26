class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'X: {self.x} \t Y: {self.y}'

    def __del__(self):
        print(f'del function called for Point X: {self.x}\tY: {self.y}', end=' ')


class Point3D(Point):
    def __init__(self, x, y, z):
        Point.__init__(self, x, y)
        self.z = z

    def __str__(self):
        return f'{Point.__str__(self)} \t Z: {self.z}\n'

    def __del__(self):
        Point.__del__(self)
        print(f'\tZ:  {self.z}')


def main():
    p = Point3D(2, 5, 3)
    print(p)


main()
