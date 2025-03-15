from bst_constructor import BinarySearchTree
from bst_constructor import Node
import contains

def insert(self, value):
    new_node = Node(value)
    if self.root is None:
        self.root=new_node
        return True
    
    temp=self.root
    while True:
        if new_node.value==temp.value:
            return False
        if new_node.value < temp.value:
            if temp.left is None:
                temp.left = new_node
                return True
            temp=temp.left
        else:
            if temp.right is None:
                temp.right =new_node
                return True
            temp=temp.right
    
    