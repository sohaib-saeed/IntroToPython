class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def set_length(self,length):
        self.length = length
    def set_width(self,width):
        self.width = width
    def __str__(self):
        return f"Length : {self.length}\nWidth: {self.width}"
class Block(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height
    def set_height(self,height):
        self.height = height
    def __str__(self):
        return f"{super().__str__()}\nHeight: {self.height}"
def main():
    r = Rectangle(1, 2)
    print(r)
    print("----------------")
    b = Block(1, 2, 3)
    print(b)
main()