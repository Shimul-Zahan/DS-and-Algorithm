class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def _lef_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, idx1, idx2):
        self.heap[idx1] , self.heap[idx2] = self.heap[idx2], self.heap[idx1]
        
    def _sink_down(self, index):
        return #Coming soon...
    
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current> 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
    
    def remove():
        return #Coming soon...
    
max_heap = MaxHeap()
max_heap.insert(99)
max_heap.insert(100)
max_heap.insert(80)
max_heap.insert(77)
max_heap.insert(520)

print(max_heap.heap)