class Student:
    def __init__(self): # constructor
        self.s_name = "Salil"
        self.l_name = "Deshpande"
        self.s_rollno = 60
        self.s_branch = "EE"
        self.s_mb = 1234567890

obj = Student()
print(obj.__dict__) 