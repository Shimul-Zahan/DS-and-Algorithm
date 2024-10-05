#create a new class for create node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# create a new class for new node
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    # Create methods
    def append(self, value):     
    def prepend(self, value):     
    def inser(self, value):     

# create a object for LinkedList class
my_linked_list = LinkedList(5)

# print the value
print(my_linked_list.head.value)