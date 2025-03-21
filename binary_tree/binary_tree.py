class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        queue = [self.root]
        print(f'This is the Queue', queue)
        while queue:
            print(f'This is the Queue', queue)
            temp = queue.pop(0)
            if not temp.left:
                print("Goes to left")
                temp.left = new_node
                return True
            else:
                print("Append to the queue left node")
                queue.append(temp.left)
            
            if not temp.right:
                print("Goes to right")
                temp.right = new_node
                return True
            else:
                print("Append to the  right node")
                queue.append(temp.right)
    
    def show(self):
        print(self.root.value)
    

bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
