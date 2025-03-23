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
    
    def bredth_first_search(self):
        current_node = self.root
        queue = []
        result = []
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return result
            
    

bt = BinaryTree()
bt.insert(1)
bt.insert(2)
bt.insert(3)
bt.insert(4)
bt.insert(5)
print("Level Order Traversal:", bt.bredth_first_search())
# Level Order Traversal:
# 1 2 3 4 5

