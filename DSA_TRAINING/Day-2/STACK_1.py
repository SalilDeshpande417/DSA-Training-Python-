import sys # It contains exit 
class Stack:
    def __init__(self,size):
        self.stackSize = size
        self.myStack = []

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False 
        
    def push(self, data):
        if self.isFull():
            print("stack is full")
        else:
            self.myStack.append(data)
            print("Element Pushed") 

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
        else:
            print(self.myStack.pop()) 

    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Top Element =",self.myStack[-1]) 

    def deleteStack(self):
        self.myStack = None
        print("Delete Stack Done") 

    def displayStack(self):
        print(self.myStack)

    def getMax(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print("Maximum Element =", max(self.myStack))


size = int(input("Enter the size of stack: ")) # execution will start from here
obj = Stack(size) 
while True:
    print("1. Push Operation :")
    print("2. POP Operation :")
    print("3. Peek Operation :")
    print("4. isEmpty Operation :")
    print("5. isFull Operation :")
    print("6. Delete Complete Operation :")
    print("7. Display Stack :")
    print("8. Get Maximum Value :")
    print("9. Exit")
    

    choice = int(input("Enter Your Choice :")) 
    if choice == 1:
        value = int(input("Enter the value to push in stack :"))
        obj.push(value) 
    elif choice == 2:
        obj.pop()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        obj.isEmpty()
    elif choice == 5:
        obj.isFull() 
    elif choice == 6:
        obj.deleteStack()
    elif choice == 7:
        obj.displayStack()
    elif choice == 8:
        obj.getMax()
    else:
        sys.exit() 

    