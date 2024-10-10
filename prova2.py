from problem_generator_improved import DirectedGraph,generate_random_graph
from FIFO_preflow_push import MaxFlow

#mf 13
graph = DirectedGraph(5)
graph.addEdge(0,1,3)
graph.addEdge(0,2,9)
graph.addEdge(0,3,6)
graph.addEdge(1,3,8)
graph.addEdge(1,4,6)
graph.addEdge(2,1,9)
graph.addEdge(2,4,7)
graph.addEdge(3,2,1)
graph.addEdge(4,3,3)
graph.addEdge(4,0,2)

mf = MaxFlow(graph,0,4)
value = mf.FIFOPushRelabel()
print(value)