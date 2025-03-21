# Here we implement the Bredth First Search (BFS)
from initial_tree import BinarySearchTree

def bredth_first_search(self):
    if not self.root:
        return []
    current_node = self.root
    queue = []
    result = []
    queue.append(current_node)
    while len(queue) > 0:
        current_node = queue.pop(0)  # pop element from the first FIFO
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return result


# ✅ Monkey patch BFS method to BinarySearchTree class
# BinarySearchTree.bredth_first_search = bredth_first_search