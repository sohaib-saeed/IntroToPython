class CollegeCourse:
    def __init__(self,dept,course_no,cr,tuition):
        self.dept = dept
        self.course_no = course_no
        self.cr = cr
        self.tution = tuition
    def set_dept(self,dept):
        self.dept = dept
    def set_course_no(self,course_no):
        self.course_no = course_no
    def set_cr(self,cr):
        self.cr = cr
    def set_tuition(self,tuition):
        self.tution = tution
    def get_dept(self):
        return self.dept
    def get_course_no(self):
        return self.course_no
    def get_cr(self):
        return self.cr
    def get_tuition(self):
        return self.tuition
    def __str__(self):
        return f"Department: {self.dept}\nCourse Number: {self.course_no}\nCredit Hours: {self.cr}\nTuition Fee: {self.tution}"
class LabCourse(CollegeCourse):
    def __init__(self,dept,course_no,cr,tuition,lab_fee):
        super().__init__(dept,course_no,cr,tuition)
        self.lab_fee = lab_fee
    def set_lab_fee(self,lab_fee):
        self.lab_fee = lab_fee
    def get_lab_fee(self):
        return lab_fee
    def __str__(self):
        return f"{super().__str__()}\n" + f"Lab Fee: {self.lab_fee}"
def main():
    l = LabCourse(1, 2, 2,4, 5)
    print(l)
main()