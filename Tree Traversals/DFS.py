# here we implement Depth First Search (DFS)

def dfs_preorder(self):
    if self.root is None:
        return []
    current_node = self.root
    result = []
    def traversal(current_node):
        print("Visiting Node:", current_node.value)
        result.append(current_node.value)
        if current_node.left:
            print(current_node, "current node for left")
            traversal(current_node.left)
        if current_node.right:
            print(current_node, "current node for right")
            traversal(current_node.right)
    traversal(self.root)
    return result

def dfs_inorder(self):
    pass
    

def dfs_postorder(self):
    current_node = self.root
    result = []
    def traversal(current_node):
        if current_node.left:
            traversal(current_node.left)
        if current_node.right:
            traversal(current_node.right)
        result.append(current_node.value)
        
    traversal(self.root)
    return result