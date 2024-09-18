#Creation and Traversal for Linked List


#Creation
class Node:
    def __init__(self,k):
        self.key = k
        self.next = None

head = Node(0)
temp1 = Node(1)
temp2 = Node(2)
head.next = temp1
head.next.next = temp2
temp1.next = temp2

#Traversal
def printing(head):
    current = head
    while current !=None:
        print(current.key, end= " -> ")
        current = current.next
printing(head) #Caller
print("")

#Searching in Linked List


#returns position of item if found, if not returns -1
def search(head, n):
    current = head
    
    pos = 0
    while current != None:
        if current.key == n:
            return pos
        elif current.next == None:
            return -1
        else:
            current = current.next
            pos += 1

print(search(head, 1))