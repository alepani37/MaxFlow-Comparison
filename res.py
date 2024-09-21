from problem_generator import DirectedGraph

def build_residual_graph(graph):
    residual_graph = DirectedGraph(graph.vertices)  # Inizializza il grafo residuo

    for u in range(graph.vertices):
        for edge in graph.adjacencyList[u]:  # Itera attraverso le adiacenze di u
            v = edge.i  # Estrai il vertice destinazione
            capacity = edge.w  # Estrai la capacità dell'arco

            # Aggiorna il grafo residuo con l'arco u -> v
            if residual_graph.hasEdge(u, v):
                residual_graph.getEdge(u, v).w += capacity
            else:
                residual_graph.addEdge(u, v, capacity)

            # Aggiungi l'arco v -> u con capacità 0 se non esiste
            if not residual_graph.hasEdge(v, u):
                residual_graph.addEdge(v, u, 0)

    return residual_graph
