class Node:
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
class BinartTree:
    def __init__(self):
        self.root=None
        
    def inser(self, value):
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
                
                
