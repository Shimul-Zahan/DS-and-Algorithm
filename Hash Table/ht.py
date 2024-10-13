class HashTable:
    def __init__(self, size = 7):
        self.data_map = [None] * size
        # print(see)
        
    def _hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = ( my_hash + ord(letter) * 23 ) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
    def set_item(self, key, value):
        index = self._hash(key) 
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])
        
    def __getitem__(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    
    def all_keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys
    
    
                
            
        
ht = HashTable()
ht.set_item("hi", 100)
ht.set_item("hello", 200)
ht.set_item("salam", 400)
ht.set_item("bye bye", 300)
# ht.print_table()

# get item
# print(ht.__getitem__("hi"), 'value')
print(ht.all_keys())
        