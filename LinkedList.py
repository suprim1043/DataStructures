#Creation and Traversal for Linked List

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
def printing(head):
    current = head
    while current !=None:
        print(current.key)
        current = current.next

printing(head)