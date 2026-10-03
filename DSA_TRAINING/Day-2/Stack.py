#class Stack:
   # def __init__(self, value):
      #  self.data = value
       # self.myStack = [] 



class Student:

    rollno = 101 # data member
    def __init__(self): # 2 byte
        print("I am constructor i always called first")

    def msg(self): # 1 byte   total memory = 3 byte (1001)
        print("Hello World")

obj = Student()
print(obj) 
obj.msg()
obj2 = Student() 
print(obj.rollno) 