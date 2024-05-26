class CollegeCourse:
    def __init__(self,dept,course_no,cr_hr,tution_fee):
        self.dept = dept
        self.course_no = course_no
        self.cr_hr = cr_hr
        self.tution_fee = tution_fee
    def set_dept(self,dept):
        self.dept = dept
    def set_course_no(self,course_no):
        self.course_no = course_no
    def set_cr_hr(self,cr_hr):
        self.cr_hr = cr_hr
    def set_tuition(self,tution_fee):
        self.tution_fee = tution_fee
    def get_dept(self):
        return self.dept
    def get_course_no(self):
        return self.course_no
    def get_cr_hr(self):
        return self.cr_hr
    def get_tuition(self):
        return self.tution_fee
    def __str__(self):
        return f"Department: {self.dept}\nCourse No: {self.course_no}\nCredit Hours: {self.cr_hr}\nTution Fee: {self.tution_fee}"
    def display(self):
        print(f"Department: {self.dept}\nCourse No: {self.course_no}\nCredit Hours: {self.cr_hr}\nTution Fee: {self.tution_fee}")

class LabCourse(CollegeCourse):
    def __init__(self,dept,course_no,cr_hr,tution_fee,lab_fee):
        super().__init__(dept,course_no,cr_hr,tution_fee)
        self.lab_fee = lab_fee
    def set_lab_fee(self,lab_fee):
        self.lab_fee = lab_fee
    def get_lab_fee(self):
        return self.lab_fee
    def __str__(self):
        return f"{super().__str__()}\nLab Fee: {self.lab_fee}"
    def display(self):
        print(f"{super().__str__()}\nLab Fee: {self.lab_fee}")
def main():
    # create a CollegeCourse object and display its fields
    cc = CollegeCourse("Mathematics", "MATH101", 3, 3000)
    cc.display()
    print()
    
    # create a LabCourse object and display its fields
    lc = LabCourse("Biology", "BIOL101", 4, 3500, 500)
    lc.display()
    print()
    
    # update the fields of the LabCourse object and display them again
    lc.set_tuition(4000)
    lc.set_lab_fee(600)
    lc.display()


if __name__ == '__main__':
    main()
    