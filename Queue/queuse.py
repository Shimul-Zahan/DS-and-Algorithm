class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
        
        
    def print(self):
        temp =  self.first
        while temp:
            print(temp.value)
            temp = temp.next
     
     
    def enqueue(self, value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node    
            self.length += 1
        return True   
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else: 
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp.value
        
            
queue = Queue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print("Deque : ", queue.dequeue())
print("Deque : ", queue.dequeue())
queue.print()
