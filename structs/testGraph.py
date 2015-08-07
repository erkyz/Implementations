from graph import Graph

test = Graph({'five':5,'ten':10})
test.addEdge("five","ten",1)
test.addVertex("seven",7)
test.addEdge("five","seven",2)
print(test.getEdges())
del test["ten"]
print(test.getEdges())
del test["seven"]
print(test.getEdges())
