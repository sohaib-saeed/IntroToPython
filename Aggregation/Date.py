class Date:
    def __init__(self,day,month,year):
        self.day = str(day)
        self.month = str(month)
        self.year = str(year)
        self.day_str = self.get_day()
        self.month_str = self.get_month()
        self.year_str = self.get_year()
    def get_day(self):
        return self.day
    def get_month(self):
        return self.month
    def get_year(self):
        return self.year
    def __str__(self):
        return f"{self.day}-{self.month}-{self.year}"
class Employee:
    def __init__(self, employee_no, name, designation, day, month, year , salary):
        self.employee_no = employee_no
        self.name = name
        self.designation = designation
        self.joing_date = Date(day, month, year)
        self.promotion_date = None
        self.salary = salary
    def set_date(self,day,month,year):
        self.promotion_date = Date(day, month, year)
    def __str__(self):
        s = ""
        s += f"Employee No: {self.employee_no}\nName: {self.name}\nDesignation: {self.designation}\nJoing Date: {self.joing_date}\n"
        if self.promotion_date is None:
            s+= "Promtion Date: No Promotion Date\n"
        else:
            s += f"Promtion Date: {self.promotion_date}\n"
        s += f"Salary: {self.salary}"
        return s

def main():
    e = Employee(123, "Sohiab", "Clerk", 12 , 10 , 2004, 50000)
    print(e)
    print("----------")
    e1 = Employee(123, "Sohiab", "Clerk", 12, 10, 2004, 50000)
    e1.set_date(12, 10, 2010)
    print(e1)
main()


