# Here I implement binary tree indepths
# 1. Root
# 2. Left Node
# 3. Right Node

class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        # new_node = Tree(value)
        self.root = None
        
    def insert(self, value):
        new_node = True(value)
        
my_tree = BinaryTree()
print(my_tree.root)