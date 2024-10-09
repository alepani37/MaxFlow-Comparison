from problem_generator_improved import DirectedGraph

class MaxFlow:
    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink
        self.h = [float("inf")] * self.graph.vertices
        self.e = [0] * self.graph.vertices
        self.queue = []

    def initResidualGraph(self):
        """Inizializza il grafo residuo in base alle capacità originali."""
        self.residualGraph = DirectedGraph(self.graph.vertices)
        for u in range(self.graph.vertices):
            for v in self.graph.adjacencyList[u]:
                if self.residualGraph.hasEdge(u, v.i):
                    self.residualGraph.getEdge(u, v.i).w += v.w
                else:
                    self.residualGraph.addEdge(u, v.i, v.w)
                if not self.residualGraph.hasEdge(v.i, u):
                    self.residualGraph.addEdge(v.i, u, 0)  # Arco inverso con capacità 0

    def computeExactDistanceLabels(self):
        """Calcola le etichette di distanza esatte dal sink."""
        queue = [self.sink]
        self.h[self.sink] = 0

        while queue:
            u = queue.pop(0)
            for v in self.residualGraph.adjacencyList[u]:
                if self.h[v.i] == float("inf") and self.residualGraph.getEdgeCapacity(v.i, u) > 0:
                    self.h[v.i] = self.h[u] + 1
                    queue.append(v.i)

    def preprocess(self):
        """Effettua il preprocessamento: inizializza le altezze e gli eccessi."""

        self.computeExactDistanceLabels()
        self.h[self.source] = self.graph.vertices
        for v in self.graph.adjacencyList[self.source]:
            cap = self.residualGraph.getEdgeCapacity(self.source, v.i)
            self.residualGraph.getEdge(self.source,v.i).w = 0  # Imposta il flusso iniziale
            self.residualGraph.getEdge(v.i,self.source).w += cap  # Arco inverso
            self.e[v.i] += cap
            self.e[self.source] -= cap

    def push(self, u, v):

        delta = min(self.e[u], self.residualGraph.getEdgeCapacity(u,v.i))
        self.residualGraph.getEdge(v.i,u).w += delta
        self.residualGraph.getEdge(u,v.i).w -= delta  # Arco inverso
        self.e[u] -= delta
        self.e[v.i] += delta

    def relabel(self, u):
        """Esegue il relabel del nodo u."""
        min_height = float("inf")
        for v in self.residualGraph.adjacencyList[u]:
            if self.residualGraph.getEdgeCapacity(u, v.i) > 0:  # Arco residuo disponibile
                min_height = min(min_height, self.h[v.i])

        if min_height < float("inf"):
            self.h[u] = min_height + 1

    def pushRelabel(self, u):
        """Procedura Push/Relabel per il nodo u."""
        # Controlla se c'è almeno un arco ammissibile per il push
        for v in self.residualGraph.adjacencyList[u]:
            if self.residualGraph.getEdgeCapacity(u, v.i) > 0 and self.h[u] == self.h[v.i] + 1:
                self.push(u, v)
                if self.e[v.i] > 0 and v.i not in self.queue and v.i != self.sink and v.i != self.source:
                    self.queue.append(v.i)  # Aggiunge v alla lista attiva se non è già presente
                if self.e[u] == 0:  # Se non c'è più eccesso su u, esci dalla funzione
                    return
                else:
                    self.queue.append(u)
        # Se non ci sono archi ammissibili, esegui il relabel
        self.relabel(u)


    def FIFOPushRelabel(self):
        """Algoritmo Push-Relabel con approccio FIFO."""

        # Coda dei nodi attivi
        self.initResidualGraph()
        # Preprocessamento: inizializza altezze ed eccessi
        self.preprocess()

        # Inizializzazione della coda dei nodi attivi (eccetto la sorgente e il sink)
        for v in self.residualGraph.adjacencyList[self.source]:
            if self.e[v.i] > 0 and v.i != self.sink and v.i != self.source:
                self.queue.append(v.i)

        # Elaborazione della coda FIFO
        while self.queue:
            u = self.queue.pop(0)
            self.pushRelabel(u)
        # Il flusso massimo è la somma dei flussi uscenti dalla sorgente
        return self.e[self.sink]