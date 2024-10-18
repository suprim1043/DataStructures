#binary tree

class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



binTree = Tree(2)

print(f'{binTree.val} -> {binTree.left} -> {binTree.right}')

