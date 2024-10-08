
from problem_generator_improved import DirectedGraph

graph = DirectedGraph(3)
graph.addEdge(0,1,1)
graph.addEdge(0,2,1)
graph.addEdge(1,2,1)

for edge in graph.getEdgesFlows():
    print(edge)


graph.addFlow(0,1,1)

print("poho")
for edge in graph.getEdgesFlows():
    print(edge)