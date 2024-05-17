class Classroom:
    def __init__(self,building,room_num):
        self.__building = building
        self.__room_num = room_num
    def set_values(self,building,room_num):
        self.__building = building
        self.__room_num = room_num
    def __str__(self):
        return f"Building: {self.__building}\nRoom Number: {self.__room_num}"
