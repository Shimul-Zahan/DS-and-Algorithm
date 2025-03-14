class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
class BinaryTree:
    def __init__(self):
        self.root=None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: return True
        return False
    
    def inorder(self):   # Left → Root → Right
        if self.root is not None:
            self.inorder(self.root.left)
            print()
                
                
my_tree=BinaryTree()
my_tree.insert(50)
my_tree.insert(20)
my_tree.insert(40)
my_tree.insert(10)
my_tree.insert(21)
print(my_tree.contains(50))