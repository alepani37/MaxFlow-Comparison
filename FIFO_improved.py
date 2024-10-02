from problem_generator import DirectedGraph
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

    def FIFOPushRelabel(self):
        self.initResidualGraph()
        queue = []
        e = [0] * self.graph.vertices
        h = [0] * self.graph.vertices
        inQueue = [False] * self.graph.vertices
        h[self.source] = self.graph.vertices
        for v in self.graph.adjacencyList[self.source]:
            print("v: " + str(v))
            self.residualGraph.getEdge(self.source, v.i).w = 0
            self.residualGraph.getEdge(v.i, self.source).w = v.w
            e[v.i] = v.w
            if v.i != self.sink:
                queue.append(v.i)
                inQueue[v.i] = True
        # Step 2: Update the pre-flow
        # while there remains an applicable
        # push or relabel operation
        while queue:
            # vertex removed from
            # queue in constant time
            u = queue.pop(0)
            inQueue[u] = False
            self.relabel(u, h)
            self.push(u, e, h, queue, inQueue)
        return e[self.sink]


    def relabel(self, u, h):
        minHeight = float("inf")
        for v in self.residualGraph.adjacencyList[u]:
            if v.w > 0:  # Check if the residual capacity is positive
                minHeight = min(minHeight, h[v.i])
        if minHeight < float("inf"):  # Only relabel if there was an adjacent vertex with capacity
            h[u] = minHeight + 1

    def push(self, u, e, h, queue, in_queue):
        for v in self.residualGraph.adjacencyList[u]:
            # after pushing flow if
            # there is no excess flow,
            # then break
            if e[u] == 0:
                break

            # push more flow to
            # the adjacent v if possible
            if v.w > 0 and h[v.i] < h[u]:
                # flow possible
                f = min(e[u], v.w)

                v.w -= f
                self.residualGraph.getEdge(v.i, u).w += f

                e[u] -= f
                e[v.i] += f

                # add the new overflowing
                # immediate vertex to queue
                if not in_queue[v.i] and v.i != self.source and v.i != self.sink:
                    queue.append(v.i)
                    in_queue[v.i] = True

        # if after sending flow to all the
        # intermediate vertices, the
        # vertex is still overflowing.
        # add it to queue again
        if e[u] != 0:
            queue.append(u)
            in_queue[u] = True