class MaxFlow:
    def __init__(self, graph, source, sink):
        self.graph = graph
        self.source = source
        self.sink = sink

    def initResidualGraph(self):
        self.residualGraph = DirectedGraph(self.graph.vertices)
        for u in range(self.graph.vertices):
            for v in self.graph.adjacencyList[u]:
                if self.residualGraph.hasEdge(u, v.i):
                    self.residualGraph.getEdge(u, v.i).w += v.w
                else:
                    self.residualGraph.addEdge(u, v.i, v.w)
                if not self.residualGraph.hasEdge(v.i, u):
                    self.residualGraph.addEdge(v.i, u, 0)

    def computeExactDistanceLabels(self):

        queue = [self.sink]
        d = [float('inf')] * self.graph.vertices
        d[self.sink] = 0

        while queue:
            u = queue.pop(0)
            for v in self.graph.adjacencyList[u]:
                if d[v] == float("inf"):
                    d[v] = d[u] + 1
                    queue.append(v)
        return d

    def preprocess(self):

        d = self.computeExactDistanceLabels()
        h = [d[i] for i in range(self.graph.vertices)]
        h[self.source] = self.graph.vertices

        for v in self.graph.adjacencyList[self.source]:
            

        return e,h

    def FIFOpreoflowPush(self):
        self.initResidualGraph()
        queue = []
        e,h = preprocess()