class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def __str__(self):
        return f"Length: {self.length}\nWidth: {self.width}"
    def get_area(self):
        return self.length * self.width
    def get_perimeter(self):
        return 2 * (self.length + self.width)
    def get_diagonal(self):
        return round((((self.width) ** 2) + ((self.length) ** 2)) ** 0.5, 2)

class Block(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def get_area_b(self):
        return self.length * self.width * self.height
    def __str__(self):
        return f"{super().__str__()}\n" + f"Height: {self.height}"
def main():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    r = Rectangle(length, width)
    print(r)
    print(f"Area of Rectangle: {r.get_area()}")
    print(f"Perimeter of Rectangle: {r.get_perimeter()}")
    print(f"Diagonal of Rectangle: {r.get_diagonal()}")
    print("--------------")
    length = float(input("Enter the Length: "))
    width = float(input("Enter the Width: "))
    height = float(input("Enter the Height: "))
    b = Block(length, width, height)
    print(b)
    print(f"Area of Block: {b.get_area_b()}")
    
main()

