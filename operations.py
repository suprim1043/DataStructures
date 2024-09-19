from LinkedList import Node,printing

#inserting a the beginning
def insertHead(head, key):
    temp = Node(key)
    temp.next = head
    return temp

head = None
head = insertHead(head, 10)
head = insertHead(head, 20)

#inserting at the end 
def insertTail(head,key):
    if head == None:
        return Node(key)

    current = head
    while current.next != None: 
        current = current.next
    current.next = Node(key)
    return head
printing(insertTail(head, 20))
