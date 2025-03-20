from initial_tree import BinarySearchTree
from BFS import bredth_first_search
from DFS import dfs_inorder, dfs_postorder, dfs_preorder

# insert = BinarySearchTree()
BinarySearchTree.bredth_first_search = bredth_first_search
BinarySearchTree.dfs_preorder = dfs_preorder
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(2)
bst.insert(7)


print("BFS Traversal:", bst.bredth_first_search())  
# ✅ Expected Output: [10, 5, 15, 2, 7]

print("Preorder Traversal:", bst.dfs_preorder())  
# Expected Output: [10, 5, 2, 7, 15]