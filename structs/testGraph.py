from graph import Graph

test = Graph({'five':5,'ten':10})
test.addEdge("five","ten",1)
test.addVertex("seven",7)
test.addEdge("five","seven",2)
print("5:",test.getConnections("five"))
print("5 to 10:", test.getWeight("five","ten"))
print("7 to 5:", test.getWeight("seven","five"))
print(test.getEdges())
del test["ten"]
print(test.getEdges())
del test["seven"]
print(test.getEdges())
