class Node:
    def __init__(self,value):
# every node contain two parts: 1. Data 2.Address
     self.data = value  # [10|None] [20|None] [30|None]
     self.next = None   # 101        102       103

class Linkedlist:
    def __init__(self): # head [None]
        self.head = None  # 101

linkedlistobj = Linkedlist() 

# create seperate nodes/memory is like creating object  
linkedlistobj.head = Node(10) 
second = Node(20)
third = Node(30) 
four = Node(40)
five = Node(50)

# connecting nodes 
linkedlistobj.head.next = second 
second.next = third 
third.next = four
four.next = five

# display linked list 
while linkedlistobj.head != None:
    print("|",linkedlistobj.head.data,"|",">",end= " ") # To print the address print("|",linkedlistobj.head.next,"|",">",end= " ")
    linkedlistobj.head = linkedlistobj.head.next 
