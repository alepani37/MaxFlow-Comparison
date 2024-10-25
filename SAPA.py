from res import build_residual_graph

class MaxFlowSAPA:
    def __init__(self, graph, source, sink):
        self.graph = build_residual_graph(graph)  # Assicurati che crei correttamente il grafo residuo
        self.source = source
        self.sink = sink
        self.n = graph.vertices  # Numero di nodi
        self.x = [[0] * self.n for _ in range(self.n)]  # Matrice dei flussi iniziale

    def shortest_augmenting_path(self):
        d = self.get_exact_distance_labels(self.sink)  # Ottenere le etichette di distanza dal sink
        pred = [-1] * self.n  # Predecessori dei nodi nel cammino di aumentazione
        i = self.source

        # Ciclo principale dell'algoritmo
        while d[self.source] < self.n:
            if self.has_admissible_arc(i, d):
                i = self.advance(i, d, pred)
                if i == self.sink:  # Se abbiamo raggiunto il sink, aumentiamo il flusso
                    self.augment(pred)
                    i = self.source  # Torniamo alla sorgente per cercare un altro cammino aumentante
            else:
                i = self.retreat(i, d, pred)  # Se non ci sono archi ammissibili, facciamo retreat
        return self.x  # Restituiamo la matrice dei flussi

    def get_exact_distance_labels(self, sink):
        d = [self.n] * self.n  # Inizializziamo le distanze al massimo possibile
        d[sink] = 0  # La distanza dal sink a se stesso è 0
        queue = [sink]  # Partiamo dal sink

        while queue:
            i = queue.pop(0)
            for vertex in self.graph.adjacencyList[i]:
                j = vertex.i
                if d[j] == self.n and self.graph.getEdge(j,i).w > 0:  # Consideriamo solo gli archi con capacità residua positiva
                    d[j] = d[i] + 1
                    queue.append(j)
        return d

    def has_admissible_arc(self, i, d):
        """Controlla se c'è un arco ammissibile da i"""
        for vertex in self.graph.adjacencyList[i]:
            j = vertex.i
            if d[i] == d[j] + 1 and vertex.w > self.x[i][j]:  # Condizione di ammissibilità
                return True
        return False

    def advance(self, i, d, pred):
        """Avanza lungo un arco ammissibile da i"""
        for vertex in self.graph.adjacencyList[i]:
            j = vertex.i
            if d[i] == d[j] + 1 and vertex.w > self.x[i][j]:
                pred[j] = i  # Tracciamo il predecessore
                return j
        return i

    def retreat(self, i, d, pred):
        """Esegui il retreat sul nodo i"""
        possible_distances = [d[vertex.i] + 1 for vertex in self.graph.adjacencyList[i] if vertex.w > self.x[i][vertex.i]]

        if possible_distances:
            d[i] = min(possible_distances)  # Aggiorniamo l'etichetta di distanza
        else:
            d[i] = self.n  # Se non ci sono archi ammissibili, assegniamo il massimo

        if i != self.source:
            i = pred[i]  # Torniamo indietro al predecessore
        return i

    def augment(self, pred):
        """Aumenta il flusso lungo il cammino trovato"""
        delta = float('inf')
        j = self.sink

        # Troviamo il minimo flusso incrementabile lungo il cammino
        while j != self.source:
            i = pred[j]
            edge = self.graph.getEdge(i, j)
            delta = min(delta, edge.w - self.x[i][j])  # Flusso incrementabile
            j = i

        # Aumentiamo il flusso lungo il cammino
        j = self.sink
        while j != self.source:
            i = pred[j]
            self.x[i][j] += delta
            self.x[j][i] -= delta  # Aggiorniamo il flusso inverso
            j = i
