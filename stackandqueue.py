#implementing stack with array

class stack():
    
    def __init__(self):
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
        return self.stack
    
    def pop(self):
        
        if len(self.stack) == 0:
            return -1    
        self.stack.pop()
        return self.stack
    
    def peek(self):
        if len(self.stack) == 0:
            return -1
        else: 
            return self.stack[-1]
        
    def isEmpty(self):
        if len(self.stack) == 0:
            return -1

    def size(self):
        return len(self.stack)
    

#stack creation

myStack = stack()


'''
print(myStack.push(1))
print(myStack.push(2))
print(myStack.pop())
print(myStack.peek())
print(myStack.push(73))
print(myStack.isEmpty())
print(myStack.size())
'''

#implementing queue using array

class queue():
    def __init__(self):
        self.queue = []
    
    def enque(self,val):
        self.queue.append(val)
        return self.queue
    
    def deque(self):
        if len(self.queue) == 0:
            return -1

        self.queue.pop(0)
        return self.queue
    
    def peek(self):
        return self.queue[0]
    
    def isEmpty(self):
        return len(self.queue) == 0

  
q = queue()
print(q.enque(2))
print(q.enque(3))
print(q.enque(4))
print(q.deque())
print(q.peek())
print(q.isEmpty())