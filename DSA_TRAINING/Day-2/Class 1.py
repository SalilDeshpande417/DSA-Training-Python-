'''class Hod:
    def __init__(self): # Constructor
        self.name = 'Salil Deshpande' # 2 Byte
        self.age = 19                 # 3 Byte
        self.empid = 1001             # 1 Byte
    def info(self): # instance method
        print("My name is :",self.name)
        print("My Age is :",self.age)
        print("My Emp Id :",self.empid)

obj = Hod() # object create 
obj.info() '''

class Hod:
    def __init__(self,name,age,rollno): # parameterize constructor
        self.name = name 
        self.age = age
        self.rollno = rollno

    def show(self):
        print('name = ',self.name)
        print('age = ',self.age)
        print('rollno = ',self.rollno)

obj = Hod('Salil', 60, 101)
obj.show() 