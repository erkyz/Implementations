from structs.avl import AVL_dict # will only work from outside structs

# using adjacency list - prefer sparse
class Graph: # weighted
    def __init__(self,items):
        self.n = 0
        self.m = 0
        self.vertices = AVL_dict({})
        for item in items:
            self.addVertex(item,items[item])

    def __getitem__(self,x):
        return self.vertices[x]

    def getWeight(self,f,t): # O(log n) - don't use.
        if f in self.vertices:
            if t in self.vertices[f]["neighbors"]:
                return self.vertices[f]["neighbors"][t]
        else:
            print(f,"not in this graph")
            return

    def getVertices(self): # O(n) 
        return list(self.vertices)

    def getConnections(self,v):
        if self.vertices[v] is None: 
            print(v, "not in this graph")
            return
        conn = []
        for neighbor,weight in self.vertices[v]['neighbors']:
            conn.append((neighbor,weight))
        return conn

    def getEdges(self): # O(m) 
        visited = []
        edges = []
        for v,val in self.vertices:
            visited.append(v)
            for w,cost in self.vertices[v]['neighbors']:
                if w not in visited:
                    edges.append((v,w,cost))
        return edges

    def addVertex(self,name,val): # O(log n)
        self.vertices.insert(name,{'val':val,'neighbors':AVL_dict({})})
        self.n += 1
        
    def addEdge(self,f,t,cost): # O(log n)
        if not self.vertices[f]:
            print('Error:', f, 'is not in this graph')
            return
        if not self.vertices[t]:
            print('Error:', t, 'is not in this graph')
            return

        vf = self.vertices[f]
        vt = self.vertices[t]

        if t in vf['neighbors']:
            print("Error: This edge already exists")
            return
        else:
            vf['neighbors'].insert(t, cost)
            vt['neighbors'].insert(f, cost)
            self.m += 1

    def __delitem__(self,x):
        del self.vertices[x]
        for v,val in self.vertices:
            if x in self.vertices[v]['neighbors']:
                del self.vertices[v]['neighbors'][x]

    def __contains__(self,x):
        return x in self.vertices


class Digraph(Graph):
    def addEdge(self,f,t,cost): # O(log n)
        if not self.vertices[f]:
            print('Error:', f, 'is not in this graph')
            return
        if not self.vertices[t]:
            print('Error:', t, 'is not in this graph')
            return

        vf = self.vertices[f]
        vt = self.vertices[t]

        if t in vf['neighbors']:
            print("Error: This edge already exists")
            return
        else:
            vf['neighbors'].insert(t, cost)
            self.m += 1

    # probably want to edit getEdges too
