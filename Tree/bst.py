# create node for a tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            self.length += 1
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    self.length += 1
                    return True
                temp = temp.left
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    self.length += 1
                    return True
                temp = temp.right
            
    # In-order Traversal (Left, Root, Right)
    def in_order_traversal(self, root):
        if root is not None:
            self.in_order_traversal(root.left)
            print(root.value)
            self.in_order_traversal(root.right)        
    
    # Pre-order Traversal (Root, Left, Right)
    def pre_order_traversal(self, node):
        if node is not None:
            print(node.value)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
    
    # Post-order Traversal (Left, Right, Root)
    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value)
            
            
my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(5)
my_tree.insert(15)
my_tree.insert(20)
my_tree.insert(25)
my_tree.insert(3)

print(my_tree.length)
print(my_tree.root.value, "root")
print(my_tree.root.left.value, "left")
print(my_tree.root.right.value, "right")
print("In-order Traversal:")
my_tree.in_order_traversal(my_tree.root) 
print("Pre-order Traversal:")
my_tree.pre_order_traversal(my_tree.root) 
print("post-order Traversal:")
my_tree.in_order_traversal(my_tree.root) 
