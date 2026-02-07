from collections import deque
class vertex :
    def __init__(self , data):
        self.data = data 
        self.next1 = None
        self.next2 = None 

class graph :
    def __init__(self):
        self.g = {}

#/////////////////////////////////////////////////////////////////////////////////////////////
    def add_vertex (self , v) :
        if v not in self.g :
            self.g [v] = []
#/////////////////////////////////////////////////////////////////////////////////////////////

    def add_edge (self ,v1 ,v2):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.g[v1].append(v2)
        self.g[v2].append(v1)

#/////////////////////////////////////////////////////////////////////////////////////////////
    def display(self) :
        for v in self.g :
            print(v , "-->" , self.g[v])

#//////////////////////////////////////////////////////////////////////////////////////////////
    

    def rec_Dfs( self , start ,visited = None):
        if visited is None :
            visited = []
        visited.append(start)
        for ne in self.g[start]  :
            if ne not in visited :
                self.rec_Dfs( ne , visited)
        return visited

#///////////////////////////////////////////////////////////////////////////////////////////////
    def BFS(self , start ):
        visited = set()
        queue = deque([start])
        visited.add(start)
        tr_order = []
        while queue:
            vertex = queue.pop()
            tr_order.append(vertex)
            for ne in self.g[vertex]:
                if ne not in visited :
                    visited.add(ne)
                    queue.append(ne)
        return tr_order

g = graph()

g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

g.display()

print (g.rec_Dfs("A"))  # A B D C E
print (g.BFS("A"))  # A B C D E

                     

        