from bst_constructor import BinarySearchTree, Node
from bst_insert import insert
from contains import contains


BinarySearchTree.insert = insert
BinarySearchTree.contains = contains
my_tree = BinarySearchTree()
print(my_tree.insert(10))
print(my_tree.insert(5))
print(my_tree.insert(15))
print(my_tree.insert(7))
print(my_tree.insert(10))
print(my_tree.contains(25))  # should be True