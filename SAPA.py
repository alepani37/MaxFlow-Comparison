from problem_generator import DirectedGraph
def shortest_augmenting_path(graph, s, t):
    n = graph.vertices  # Numero di nodi
    x = [[0] * n for _ in range(n)]  # Flusso iniziale zero
    d = get_exact_distance_labels(graph, s)  # Ottenere le etichette di distanza esatte
    pred = [-1] * n  # Predecessori dei nodi nel cammino di aumentazione
    i = s

    while d[s] < n:
        if has_admissible_arc(graph, x, d, i):
            i = advance(i, graph, x, d, pred)
            if i == t:
                augment(graph, x, pred, s, t)
                i = s
        else:
            i = retreat(i, graph, x, d, pred, s)

    return x


def get_exact_distance_labels(graph, s):
    n = graph.vertices
    d = [n] * n
    d[s] = 0
    queue = [s]

    while queue:
        i = queue.pop(0)
        for vertex in graph.adjacencyList[i]:
            j = vertex.i
            if d[j] == n:  # Nodo non ancora visitato
                d[j] = d[i] + 1
                queue.append(j)
    return d


def has_admissible_arc(graph, x, d, i):
    for vertex in graph.adjacencyList[i]:
        j = vertex.i
        if d[i] == d[j] + 1 and vertex.w > x[i][j]:
            return True
    return False


def advance(i, graph, x, d, pred):
    for vertex in graph.adjacencyList[i]:
        j = vertex.i
        if d[i] == d[j] + 1 and vertex.w > x[i][j]:
            pred[j] = i
            return j
    return i


def retreat(i, graph, x, d, pred, s):
    # Trova tutte le nuove possibili distanze per il nodo i
    possible_distances = [d[vertex.i] + 1 for vertex in graph.adjacencyList[i] if vertex.w > x[i][vertex.i]]

    if possible_distances:
        d[i] = min(possible_distances)
    else:
        d[i] = len(graph.adjacencyList)  # Assegna un valore grande se non ci sono archi ammissibili

    if i != s:
        i = pred[i]
    return i


def augment(graph, x, pred, s, t):
    delta = float('inf')
    j = t
    while j != s:
        i = pred[j]
        edge = graph.getEdge(i, j)
        delta = min(delta, edge.w - x[i][j])
        j = i

    j = t
    while j != s:
        i = pred[j]
        x[i][j] += delta
        x[j][i] -= delta
        j = i

graph = DirectedGraph(6)
graph.addEdge(0, 1, 10)
graph.addEdge(0, 2, 5)
graph.addEdge(0, 3, 15)
graph.addEdge(1, 2, 4)
graph.addEdge(1, 4, 9)
graph.addEdge(1, 5, 15)
graph.addEdge(2, 3, 4)
graph.addEdge(2, 4, 8)
graph.addEdge(3, 5, 16)
graph.addEdge(4, 5, 10)

s = 0  # Nodo sorgente
t = 5  # Nodo destinazione

max_flow = shortest_augmenting_path(graph, s, t)
print("Flusso massimo:", max_flow)