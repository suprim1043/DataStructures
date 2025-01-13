#Designing a singly linked list
class Node():
    def __init__(self, key, next_node = None):
        self.key = key
        self.next = next_node

class LinkedList():
    def __init__(self):
        self.head = None

    #adds node     
    def addNode(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    #prints list        
    def printList(self):
        val = self.head
        while val:
            print(val.key, "->", end=" ")
            val = val.next
    
    def findLength(self):
        n = 0
        val = self.head
        while val:
            n += 1
            val = val.next
        print("\n")

    def searchFor(self, target):
        val = self.head
        n = 0
        while val:
            n += 1
            if val.key == target:
                return ("Value found at position",n)
            val = val.next
        return("Value not found")
   
    def addingattheBeginning(self, data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return self.head


    def addingAtSpecific(self, index, data):
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head  = new_node
            return self.head

        n = 1
        current = self.head
        while current and n < index:
            current = current.next
            n += 1
        


        new_node.next = current.next
        current.next = new_node
        return self.head

     






Linkedlst = LinkedList()
Linkedlst.addNode(3)
Linkedlst.addNode(4)
Linkedlst.addNode(5)

#Calling Methods
Linkedlst.printList()
Linkedlst.findLength()
Linkedlst.addingattheBeginning(2)



Linkedlst.addingAtSpecific(2,10)
Linkedlst.printList()


