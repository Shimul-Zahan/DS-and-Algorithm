class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            print(f"Inserted root: {new_node.value}")
            return True
        temp = self.root
        while True:
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    print(f"Inserted {new_node.value} to the left of {temp.value}")
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    print(f"Inserted {new_node.value} to the right of {temp.value}")
                    return True
                temp = temp.right
                
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)

                
                