from linkedList import Node,printing

#inserting a the beginning
def insertHead(head, key):
    temp = Node(key)
    temp.next = head
    return temp

head = None
head = insertHead(head, 10)
head = insertHead(head, 20)
head = insertHead(head, 30)

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


#Delete a node with a pointer given to it

def deletePointed(nodePnt):
    current = nodePnt.next
    nodePnt.key = current.key
    nodePnt.next = current.next


deletePointed(head)




#NEETCODE HARD 75


#Duplicate Integer return true if integer is more than 1

nums = [1,2,3,4,4]

def duplicate(nums):
    i = 0
    a = 0
    nums.sort()
    while i < len(nums) and i+1 < len(nums):
        if nums[i] == nums[i+1]:
            a += 1
        i += 1
    if a > 0: 
        return True
    else: 
        return False


#IS anagram

s = 'carrace'
t = 'racecar'

def isAnagram(s,t):
        alpha = ''.join(sorted(s))
        beta = ''.join(sorted(t))
        if alpha == beta:
            return True
        else:
            return False
    