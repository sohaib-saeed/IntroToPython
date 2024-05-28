class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z


    def set_x(self,x):
        self.x = x


    def set_y(self,y):
        self.y = y


    def set_z(self,z):
        self.z = z


    def __str__(self):
        s = ""
        if self.y > 0:
            s += f"{self.x}i + "
        else:
            s += f"{self.x}i "
        if self.z > 0:
            s += f"{self.y}j + "
        else:
            s += f"{self.y}j "
        s += f"{self.z}k"
        return s


    def __add__(self,other):
        new_vector = Vector(0,0,0)
        new_vector.x = self.x + other.x
        new_vector.y = self.y + other.y 
        new_vector.z = self.z + other.z 
        return new_vector


    def unit_vector(self):
        new_vector =  Vector(0,0,0)
        magnitude= round((self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5,2)
        new_vector.x = round(self.x / magnitude,2)
        new_vector.y = round(self.y / magnitude,2)
        new_vector.z = round(self.z / magnitude,2)
        return new_vector


    def scalar_multiplication(self, num):
        new_vector = Vector(0, 0, 0)
        new_vector.x = self.x * num
        new_vector.y = self.y * num
        new_vector.z = self.z * num
        return new_vector


    def __mul__(self, other): # cross product
        new_vector = Vector(0, 0, 0)
        new_vector.x = self.y * other.z - self.z * other.y
        new_vector.y = self.z * other.x - self.x * other.z
        new_vector.z = self.x * other.y - self.y * other.x
        return new_vector


    def __eq__(self,other):
        return self.x == other.x and self.y == other.y and self.z == othe.z


    def stp(self, v2, v3): # scalar triple product
        s = self.x * (v2.y * v3.z - v3.y * v2.z) - self.y * (v2.x * v3.z - v3.x * v2.z) + self.z * (v2.x * v3.y - v3.x * v2.y)
        return s


def main():
    v1 = Vector(2,1,5)
    v2 = Vector(3,-2,4)
    v3 = Vector(4,-1,-2)
    v3 = v1 + v3
    print("Addition of vectors: ",v3)
    print()
    v3 = v1 * v2
    print("Multiplication of vectors: ",v3)
    print()
    print("Scalar multiplication of vectors: ",v2.scalar_multiplication(3))
    print()
    if v1 == v2: #Equality_check
        print("Vectors are equal")
    else:
        print("Vectors are not equal")
    print()
    print("Unit vectors: ",v2.unit_vector())
    print()
    print("Scalar triple product: ",Vector.stp(v1, v2, v3))
main()
