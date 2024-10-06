# create node for a tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            
my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(5)
my_tree.insert(15)
my_tree.insert(20)
my_tree.insert(25)
my_tree.insert(3)

print(my_tree.root.value, "root")
print(my_tree.root.left.value, "left")
print(my_tree.root.right.value, "right")
