class Graph:
    def __init__(self):
        self.adj_list = {}
        # print(self.adj_list)
        
    def print(self):
        for vertex in self.adj_list:
            print(vertex , " : " , self.adj_list[vertex])
        
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False
    
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertext in self.adj_list[vertex]:
                self.adj_list[other_vertext].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
        
        
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A","B")
graph.add_edge("B","C")
graph.add_edge("C","A")
graph.add_edge("C","D")
graph.add_edge("A","D")

graph.print()

graph.remove_vertex("D")

# graph.remove_edge("A","B")
# graph.remove_edge("A", "D")
graph.print()
