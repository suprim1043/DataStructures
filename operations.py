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




#Delete first node of linked list

def deleteFirst(head):
    if head == None:
        return None
    else:
        return head.next


#Delete last node of linked list

def deleteLast(head):
    if head == None:
        return None
    
    current,prev = head, None
   
    while current != None:
        if current.next == None:
            current.key = None
            return head
        current = current.next
    return head
printing(deleteLast(head))