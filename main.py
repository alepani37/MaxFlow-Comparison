from FIFO import MaxFlow
from problem_generator import DirectedGraph,generate_random_graph
from SAPA import MaxFlowSAPA
import time
from numpy import mean,std
from res import build_residual_graph

loop = True
ver = int(input("Insert the number of nodes:"))
edg = float(input("Insert the number of edges:"))
wei = int(input("Insert the max capacity of the graph edges:"))


graph = generate_random_graph(ver,edg,wei)
for edge in graph.getEdges():
    print(edge)

while loop:
    choose = input("Press 1 to run FIFO preflow push algorithm\nPress 2 to run Shortest Augmenting Path algorithm.\n3 exit.\n")
    if choose == "3":
        loop = False
        continue
    experiment_rep = int(int(input("Insert the number of experiments:")))
    time_rep = []
    max_flow_list = []
    if choose == "1":
        source = int(input("Insert the source node:"))
        sink = int(input("Insert the sink node:"))
        for i in range(experiment_rep):
            start = time.time()
            maxFlow = MaxFlow(graph, source, sink)
            max_flow_list.append(maxFlow.FIFOPushRelabel())
            end = time.time()
            time_rep.append(end-start)
        mean_time = mean(time_rep)
        std_time = std(time_rep)
        print(time_rep)
        print(f"mean time FIFO: {mean_time}")
        print(f"std time FIFO: {std_time}")
        print(f"max flow FIFO: {max_flow_list}")
    if choose == "2":
        source = int(input("Insert the source node:"))
        sink = int(input("Insert the sink node:"))
        for i in range(experiment_rep):
            start = time.time()
            maxFlow = MaxFlowSAPA(graph,source,sink)
            flow = maxFlow.shortest_augmenting_path()
            max_flow_list.append(sum(flow[0]))
            end = time.time()
            time_rep.append(end-start)
        mean_time = mean(time_rep)
        print(time_rep)
        std_time = std(time_rep)
        print(f"mean time SAPA: {mean_time}")
        print(f"std time SAPA: {std_time}")
        print(f"max flow SAPA: {max_flow_list}")




