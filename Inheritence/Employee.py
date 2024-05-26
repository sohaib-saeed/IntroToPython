class Employee:
    def __init__(self,emp_name,emp_no):
        self.emp_name = emp_name
        self.emp_no = emp_no
    def __str__(self):
        return f"Employee Name: {self.emp_name}\nEmployee Number: {self.emp_no}"

class ProductionWorker(Employee):
    def __init__(self,emp_name,emp_no,shift_no,pay_per_hour):
        super().__init__(emp_no,emp_name)
        self.shift_no = shift_no
        self.pay_per_hour = pay_per_hour
        self.set_workday(shift_no)
    def set_workday(self,shift_no):
        if shift_no == 1:
            self.shift_no = "Day Shift"
        else:
            self.shift_no = "Night Shift"
    def __str__(self):
        return f"{super().__str__()}\n" + f'Shift Number: {self.shift_no}\nHour Per Hour: ${self.pay_per_hour}'
def main():
    emp_name = str(input("Enter the Employee Name: "))
    emp_no = int(input("Enter the Employee Number: "))
    shift_no = int(input("Enter the shift Number: "))
    pay_per_hour = float(input("Enter the pay her hour: "))
    p = ProductionWorker(emp_name, emp_no, shift_no, pay_per_hour)
    print("-----------------")
    print(p)
main()