
from problem_generator_improved import DirectedGraph
from FIFO_preflow_push import MaxFlow
import networkx as nx
from networkx.algorithms.flow import preflow_push
from SAPA import MaxFlowSAPA
from check_path import isReachable



graph = DirectedGraph(6)
graph.addEdge(0,1,3)
graph.addEdge(0,2,7)
graph.addEdge(1,3,3)
graph.addEdge(1,4,4)
graph.addEdge(2,1,5)
graph.addEdge(2,4,3)
graph.addEdge(3,5,2)
graph.addEdge(3,4,3)
graph.addEdge(4,5,6)


print(isReachable(graph,0,5))

mfsapa = MaxFlowSAPA(graph,0,5)

flow = mfsapa.shortest_augmenting_path()
print(sum(flow[0]))


mf = MaxFlow(graph,0,5)
print(mf.FIFOPushRelabel())

G = nx.DiGraph()
G.add_edge(0,1,capacity = 3)
G.add_edge(0,2,capacity =7)
G.add_edge(1,3,capacity =3)
G.add_edge(1,4,capacity =4)
G.add_edge(2,1,capacity =5)
G.add_edge(2,4,capacity =3)
G.add_edge(3,5,capacity =2)
G.add_edge(3,4,capacity =3)
G.add_edge(4,5,capacity =6)

nxfv,fd = nx.maximum_flow(G,0,5,flow_func=preflow_push)
print(nxfv)
