class Tree:
    def __init__(self,data):
       self.data = data 
       self.child = [] # list is used to represnt the Tree DSA

    def addChild(self,value):
        self.child.append(value)

    def __str__(self,level=0):
        ret =" "* level +str(self.data) + "\n"
        for child in self.child:
            ret += child.__str__(level+1)
        return ret
    
# create nodes

rootNode = Tree("Drinks")     
hot = Tree ("Hot")
cold = Tree("Cold")
Tea = Tree("Tea")
Coffee = Tree("Coffee")
Non_Alcoholic = Tree("Non-Alcoholic")
Alcoholic = Tree("Alcoholic")


# add Child nodes
rootNode.addChild(hot) 
rootNode.addChild(cold) 

hot.addChild(Tea) 
hot.addChild(Coffee) 

cold.addChild(Non_Alcoholic)
cold.addChild(Alcoholic) 

# print root node object
print(rootNode)  