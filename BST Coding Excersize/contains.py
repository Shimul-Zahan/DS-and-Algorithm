from bst_constructor import BinarySearchTree, Node
import bst_insert

def contains(self, value):
    
    """This function is responsible for search the value is in the tree or not"""
    
    if self.root is None:
            return False
        
    temp = self.root
    while temp:
        if value < temp.value:
            temp = temp.left
        elif value > temp.value:
            temp=temp.right
        else: return True
    return False