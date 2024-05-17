from Instuctor import *
from ClassRoom import *
class CollegeCourse:
    def __init__(self,first_name,last_name,ph_num,building,room_num,No_of_credits):
        self.__instructor = Instuctor(first_name, last_name, ph_num)
        self.__classroom = Classroom(building, room_num)
        self.__No_of_credits = No_of_credits
    def __str__(self):
        return f"{self.__instructor}\n{self.__classroom}\nNo of credits: {self.__No_of_credits}"
    def __del__(self):
        print(f"Object is deleted")
def main():
    c = CollegeCourse(
        "Sohaib", "Saeed", "03224892531", "ABC", "3-A", 18)
    print(c)
    print("---------------------")
    c2 = CollegeCourse(
        "Ali", "Saeed", "03234879502", "XYZ", "31-A", 19)
    print(c2)
main()