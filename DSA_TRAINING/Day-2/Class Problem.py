class Students:
    def __init__(self,name,mobileno,email): # parameterize constructor
        self.name = name 
        self.mobileno = mobileno
        self.email = email

    def show(self):
        print('name = ',self.name)
        print('mobileno = ',self.mobileno)
        print('email = ',self.email)

obj = Students('Salil', 9322766061, '1234@gmail.com')
obj.show() 