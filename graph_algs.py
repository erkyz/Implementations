from structs.graph import *
from structs.heap import MinHeap

# TODO make a fibonnaci heap

# REQUIRES getWeight(v) > 0 \forall v \in vertices
# REQUIRES G is Digraph and acyclic??
# ENSURES solves single-source shortest-paths problem, since single-pair problem has same complexity (makes sense..)
# if you split edges into weight-1 edges, you can see how BFS does the same thing by picking "lowest priority"
# Technicality: a path is a list of edges, but I'm returning a list of endpoints ("shortest path tree")
def Dijkstra(G,a):
    if not a in G:
        print ("Error:",a,"is not in this graph")
        return

    S = []
    visited = {}
    d = {a:0}
    # could store predecessors in p = {}
    # store costs elsewhere too since find in heap is O(n)
    pq = MinHeap([(0,(a,None))]) # (est,(curr,prev))
    for v,val in G.vertices:
        pq.insert((float("inf"),(v,None)))
        d[v] = float("inf")
        visited[v] = False

    while not pq.size == 0:
        # could implement pq with decrease-key, but that requires a hash table and I'm lazy
        curr = pq.pop()
        if visited[curr[1][0]]:
            continue
        visited[curr[1][0]] = True
        S.append(curr)
        for w,weight in G.getConnections(curr):
            # relax
            # a fib heap would be more efficient (amortized) here if E \notin O(V^2 / log V)
            if curr[0] + weight < d[w]:
                d[w] = curr[0] + weight
                pq.insert((d[w],(w,v)))

    return S


# allows negative edge weights, detects negative cycles
# reverse all edges to get shortest path /to/ single destination
# O(|V|*|E|)
def BellmanFord(G,a):
    return 
    d = {a:0}
    p = {a:None} # predecessors
    for v,val in G.vertices:
        d[v] = float("inf")
        p[v] = None
    edges = G.getEdges()
    
    for i in range(G.n):
        for v,w,cost in edges:
            # relax
            if d[v] + cost < d[w]:
                d[w] = d[v] + cost
                p[w] = v
    
    for v,w,cost in edges:
        if d[v] > cost + d[w]:
            return None # there was a negative cycle

    return d

'''
The basic idea of SPFA is the same as Bellman–Ford algorithm in that each vertex is used as a candidate to relax its adjacent vertices. The improvement over the latter is that instead of trying all vertices blindly, SPFA maintains a queue of candidate vertices and adds a vertex to the queue only if that vertex is relaxed.
'''

# good description: http://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html
# In essence, combine greedy best-first search w/ Dijkstra. if h(x) = 0, then A* = Dijkstra's, but needs a destination.
# REQUIRE h is monotonic (basically obeys triangle inequality)
def AStar(G,h,a,b):
    return 
    ''' PSEUDOCODE
    check if a is in graph
    closed = {}
    open = MinHeap([0,a])
    for all vertices:
        g[v] = float("inf") # Dijkstra d estimate
        f[v] = g[v] + h(v,b) # total estimate
        p[v] = None # predecessors
    while open is not empty:
        curr = open.pop()
        if curr = b:
            return the path along p -> p[curr] -> ... -> None

        remove curr from open, add curr to closed
        for neighbors of curr:
            if neighbor in closed: continue
            if neighbor not in open or d[curr] + w(curr,neighbor) < d[neighbor]: 
                # relax
                p[neighbor] = curr
                g[neighbor] = d[curr] + w(curr,neighbor)
                f[neighbor] = g[neighbor] + h(neighbor,b)
                if neighbor not in open: open.insert(d[neighbor],neighbor) 

    print (b, "is not in this graph")
    return None
    '''
