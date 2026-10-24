class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None  #head is starting node
        self.tail = None   # tail is last node

    # add node at the end
    def addNodeEnd(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def displayLinkedList(self):
        current = self.head
        while current is not None:
            print("|", current.data, "|", ">", end=" ")
            current = current.next
        print("None")

linkedobj = LinkedList()
linkedobj.addNodeEnd(10)
linkedobj.addNodeEnd(20)
linkedobj.addNodeEnd(30)
linkedobj.displayLinkedList() 