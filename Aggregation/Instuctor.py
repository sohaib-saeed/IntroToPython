class Instuctor:
    def __init__(self, first_name,last_name,ph_num):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__ph_num = ph_num
    def set_values(self,first_name,last_name,ph_num):
        self.__first_name = first_name
        self.__last_name = second_name
        self.__ph_num = ph_num
    def __str__(self):
        return f"First Name: {self.__first_name}\nSecond Name: {self.__last_name}\nPhone Number: {self.__ph_num}"
