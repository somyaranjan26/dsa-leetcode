num_nodes = 5
edges = [(0,1), (0, 4), (1, 2), (1, 3), (1, 4), (2,3), (3, 4)]

class Graph:
    def __init__(self, num_node, edges):
        self.num_node = num_node
        self.data = [[] for _ in range(num_node)]
        
        self.setEdge(edges)

    def __repr__(self) -> str:
        return "\n".join(["{}: {}".format(n, neighors) for n, neighors in enumerate(self.data)])
    
    def __str__(self) -> str:
        return self.__repr__()
    
    def setEdge(self, edge):
        for n1, n2 in edge:
            self.data[n1].append(n2)
            self.data[n2].append(n1)
            
    def delEdge(self, edge):
        for n1, n2 in edge:
            self.data[n1].remove(n2)
            self.data[n2].remove(n1)
            
        
graph1 = Graph(num_nodes, edges)            

print("\n",graph1)

edge = [(2, 4)]
graph1.setEdge(edge)
print("\n",graph1)
        
edge = [(2, 4)]
graph1.delEdge(edge)
print("\n",graph1)
        