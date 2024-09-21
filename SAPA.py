from res import build_residual_graph

class MaxFlowSAPA:
    def __init__(self, graph, source, sink):
        self.graph = build_residual_graph(graph)
        self.source = source
        self.sink = sink
        self.n = graph.vertices  # Numero di nodi
        self.x = [[0] * self.n for _ in range(self.n)]  # Flusso iniziale zero

    def shortest_augmenting_path(self):
        d = self.get_exact_distance_labels(self.source)  # Ottenere le etichette di distanza esatte
        pred = [-1] * self.n  # Predecessori dei nodi nel cammino di aumentazione
        i = self.source

        while d[self.source] < self.n:
            if self.has_admissible_arc(i, d):
                i = self.advance(i, d, pred)
                if i == self.sink:
                    self.augment(pred)
                    i = self.source
            else:
                i = self.retreat(i, d, pred)

        return self.x

    def get_exact_distance_labels(self, s):
        d = [self.n] * self.n
        d[s] = 0
        queue = [s]

        while queue:
            i = queue.pop(0)
            for vertex in self.graph.adjacencyList[i]:
                j = vertex.i
                if d[j] == self.n:  # Nodo non ancora visitato
                    d[j] = d[i] + 1
                    queue.append(j)
        return d

    def has_admissible_arc(self, i, d):
        for vertex in self.graph.adjacencyList[i]:
            j = vertex.i
            if d[i] == d[j] + 1 and vertex.w > self.x[i][j]:
                return True
        return False

    def advance(self, i, d, pred):
        for vertex in self.graph.adjacencyList[i]:
            j = vertex.i
            if d[i] == d[j] + 1 and vertex.w > self.x[i][j]:
                pred[j] = i
                return j
        return i

    def retreat(self, i, d, pred):
        possible_distances = [d[vertex.i] + 1 for vertex in self.graph.adjacencyList[i] if vertex.w > self.x[i][vertex.i]]

        if possible_distances:
            d[i] = min(possible_distances)
        else:
            d[i] = len(self.graph.adjacencyList)  # Assegna un valore grande se non ci sono archi ammissibili

        if i != self.source:
            i = pred[i]
        return i

    def augment(self, pred):
        delta = float('inf')
        j = self.sink
        while j != self.source:
            i = pred[j]
            edge = self.graph.getEdge(i, j)
            delta = min(delta, edge.w - self.x[i][j])
            j = i

        j = self.sink
        while j != self.source:
            i = pred[j]
            self.x[i][j] += delta
            self.x[j][i] -= delta
            j = i