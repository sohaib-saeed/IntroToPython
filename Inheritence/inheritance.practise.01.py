class Employee:
    def __init__(self,emp_no,emp_name):
        self.emp_no = emp_no
        self.emp_name = emp_name
    def set_emp_no(self,emp_no):
        self.emp_no = emp_no
    def set_emp_name(self,name):
        self.name = name
    def __str__(self):
        return f"Employee Number: {self.emp_no}\nEmployee Name: {self.emp_name}"
class ProductionWorker(Employee):
    def __init__(self,emp_no,emp_name,shift_no,hourly_pay_rate):
        super().__init__(emp_no,emp_name)
        self.shift_no = shift_no
        self.hourly_pay_rate = hourly_pay_rate
        self.set_shift_no(shift_no)
    def set_shift_no(self,shift_no):
        if shift_no == 1:
            self.shift_no ="Day"
        elif shift_no == 2:
            slf.shift_no = "Night"
    def get_shift_no(self):
        return self.shift_no
    def __str__(self):
        return f"{super().__str__()}\n" + f"Shift Number: {self.shift_no}\nHourly Pay Rate: {self.hourly_pay_rate}"
def main():
    p = ProductionWorker(1, "s", 1, 20)
    print(p)
main()
        
    