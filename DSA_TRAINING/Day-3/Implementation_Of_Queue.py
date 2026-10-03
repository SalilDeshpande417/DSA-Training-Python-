import sys

class Queue:
    def __init__(self,size):
         self.queueSize = size
         self.myQueue = []  # implementing queue using list

    def isFull(self):
            if len(self.myQueue) == self.queueSize:
                return True
            else:
                return False
    
    def isEmpty(self):
            if self.myQueue == []:
                return True
            else:
                return False 

    def enQueue(self, value):
         if self.isFull():
            print("Queue is full")
         else:
            self.myQueue.append(value)
            print("Element Pushed") 

    def deQueue(self):
         if self.isEmpty():
            print("Queue is empty")
         else:
            print(self.myQueue.pop(0)) 

    def peekFrontElement(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.myQueue[0]) 

    def deleteentireQueue(self):
        self.myQueue = None
        print("Entire Queue has Deleted") 

    def displayQueue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.myQueue)

size = int(input("Enter the size of Queue: ")) # execution will start from here
obj = Queue(size) # if we create object inside the while loop , it will create new values , old values will get deleted
while True:
    print("1. Enqueue Operation :")
    print("2. Dequeue Operation :")
    print("3. Peek Front Element Operation :")
    print("4. isEmpty Operation :")
    print("5. isFull Operation :")
    print("6. Delete Entire Queue Operation :")
    print("7. Display Queue :")
    print("8. Exit") 

    choice = int(input("Enter Your Choice :")) 
    if choice == 1:
        value = int(input("Enter the value to push in Queue :"))
        obj.enQueue(value) 
    elif choice == 2:
        obj.deQueue()
    elif choice == 3:
        obj.peekFrontElement()
    elif choice == 4:
        print(obj.isEmpty())
    elif choice == 5:
        print(obj.isFull() )
    elif choice == 6:
         obj.deleteentireQueue()
    elif choice == 7:
        obj.displayQueue()
    else:
        sys.exit() 