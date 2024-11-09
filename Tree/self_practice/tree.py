class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value) 
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                # যদি রুট এর বামে কিছু থাকে তাইলে তুমি রুট এর ভ্যালু বাড়ায়ে আবার চেক কর।
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def constains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
        
tree = BST()
tree.insert(10)
tree.insert(16)
tree.insert(33)
print("Value in tree", tree.constains(8))
print("roote here", tree.root.value)
print("Left child here", tree.root.left and tree.root.left.value)
print("Right child here", tree.root.right and tree.root.right.value)