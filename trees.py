#Binary Tree Implementation
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None :
            self.root = Node(data)
        return self.root
    def addLeft(self, val):
        if self.left is None:
            self.left = Node(val)
        return self.root
    def addRight(self, val):
        if self.right is None:
            self.right = None
        return self.root
    
   
tree = BinaryTree()
print(tree.insert(2).val)
print(tree.addLeft(2).left)
print(tree.addRight(2).right)
