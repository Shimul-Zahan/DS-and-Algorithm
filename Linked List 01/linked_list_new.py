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
            
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp.value
    
    def get(self, index): 
        if index < 0 or index >= self.length :
            return None 
        temp = self.head 
        for _ in range(index):
            temp = temp.next
        return temp
    
    
    def inser(self, index, value): 
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.pop_first()
        if index == self.length - 1 :
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return True
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
    
# create a object for LinkedList class
my_linked_list = LinkedList(0)
for i in range(0, 5):
    if i == 5:
        continue
    my_linked_list.append(i+1)
    
my_linked_list.reverse()  
my_linked_list.print_list()
# my_linked_list.remove(3)
# my_linked_list.inser(2, 30)
# my_linked_list.print_list()
# index = 5
# print(f'Index {index} element:', my_linked_list.get(index))

    
# my_linked_list.pop_first()


# my_linked_list.prepend(-1)
# my_linked_list.print_list()


# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
# print('\n popped item',my_linked_list.pop())
