from FIFO import MaxFlow
from problem_generator import DirectedGraph,generate_random_graph
from SAPA import shortest_augmenting_path

graph = generate_random_graph(6,10,0.7)
for edge in graph.getEdges():
    print(edge)
source = 0
sink = 4
maxFlow = MaxFlow(graph,source,sink)
print("\n\nMax flow with FIFO:", maxFlow.FIFOPushRelabel())
max_flow_list = shortest_augmenting_path(graph, source, sink)
max_flow = sum(max_flow_list[0])
print("Max flow with Shortest Augmenting Path algorithm:", max_flow)


