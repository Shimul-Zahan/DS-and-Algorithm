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
   
    # printing the linked list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    

    # printing the linked list
    def pop(self):
        if self.length == 0 :
            return None
        temp = self.head
        pre = self.head
        while(temp.next is not None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None  
        return temp.value    
        
    # Create methods
    def append(self, value): 
        new_node = Node(value)
        if self.head is None:
            # print('function is call')
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def prepend(self, value): 
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
            
        
    # def inser(self, value): 
    
    
# create a object for LinkedList class
my_linked_list = LinkedList(0)
for i in range(0, 5):
    if i == 5:
        continue
    my_linked_list.append(i+1)
    

my_linked_list.print_list()

my_linked_list.prepend(-1)
my_linked_list.print_list()


# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())