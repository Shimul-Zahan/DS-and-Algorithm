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
                
    def DFS_Preorder(self):
        result= []
        def traversal(currrent_node):
            result.append(currrent_node.value)
            if currrent_node.left:
                traversal(currrent_node.left)
            if currrent_node.right:
                traversal(currrent_node.right)
        traversal(self.root)
        return result
        
            
        
        
tree = BST()
tree.insert(10)
tree.insert(16)
tree.insert(5)
tree.insert(7)
tree.insert(11)
print("roote here", tree.root.value)
print("Left child here", tree.root.left and tree.root.left.value)
print("Right child here", tree.root.right and tree.root.right.value)
print(tree.DFS_Preorder())