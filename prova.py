
from problem_generator_improved import DirectedGraph,generate_random_graph
from FIFO_preflow_push import MaxFlow
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path
from SAPA import MaxFlowSAPA
from check_path import isReachable
from tqdm import tqdm


same = 0
diff = 0
n = 5
u = 10
m = 8
flag = True

for i in tqdm(range(100000)):
    while flag:
        grafo_mio,_ = generate_random_graph(n,m,u)
        if isReachable(grafo_mio,0,n-1):
            flag = False
        else:
            del grafo_mio

    pref_push = MaxFlow(grafo_mio, 0, n - 1)
    mf_fifo = pref_push.FIFOPushRelabel()


    mf_mio = MaxFlowSAPA(grafo_mio,0,n-1)
    mf_mio_value_list = mf_mio.shortest_augmenting_path()
    mf_mio_value = sum(mf_mio_value_list[0])
    

    

    if mf_mio_value == mf_fifo:
        same = same + 1
    else:
        diff = diff + 1
        print(f"flow sapa iter{i+1}: {mf_mio_value}")
        print(f"flow fifo iter{i+1}: {mf_fifo}")
        for edge in grafo_mio.getEdges():
            print(edge)
        print(pref_push.d)
    del grafo_mio
    flag = True

print(f"same:{same}, diff: {diff} ")

