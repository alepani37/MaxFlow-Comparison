import random

class Vertex:
    def __init__(self, i, w,flow = 0):
        # numero del vertice finale
        # peso o capacità associata all'arco
        self.i = i
        self.w = w
        self.flow = flow


class DirectedGraph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjacencyList = [[] for i in range(vertices)]

    def addEdge(self, u, v, weight):
        self.adjacencyList[u].append(Vertex(v, weight))

    def hasEdge(self, u, v):
        if u >= self.vertices:
            return False
        for vertex in self.adjacencyList[u]:
            if vertex.i == v:
                return True
        return False

    def getEdge(self, u, v):
        for vertex in self.adjacencyList[u]:
            if vertex.i == v:
                return vertex
        return None

    def getFlow(self, u, v):
        for vertex in self.adjacencyList[u]:
            if vertex.i == v:
                return vertex.flow
        return None

    def removeEdge(self, u, v):
        for j in self.adjacencyList[u]:
            if j.i == v:
                self.adjacencyList[u].remove(j)
        return None

    def addEdgeFlow(self, u, v,weight ,flow):

        self.adjacencyList[u].append(Vertex(v, weight,flow))

    def addFlow(self, u, v, flow):
        if self.hasEdge(u, v):
            vert = self.getEdge(u,v)
            if vert.w >= flow:
                self.removeEdge(u,v)
                self.addEdgeFlow(u,v,vert.w,flow)
            else:
                return None


    def getEdgeCapacity(self, u, v):
        for vertex in self.adjacencyList[u]:
            if vertex.i == v:
                return vertex.w
        return None

    def __str__(self):
        result = ""
        for i in range(self.vertices):
            result += f"{i}:"
            for vertex in self.adjacencyList[i]:
                result += f" -> {vertex.i} (weight {vertex.w})"
            result += "\n"
        return result

    def getEdges(self):
        edges = []
        for u in range(self.vertices):
            for vertex in self.adjacencyList[u]:
                edges.append((u, vertex.i, vertex.w))
        return edges

    def getEdgesFlows(self):
        edges = []
        for u in range(self.vertices):
            for vertex in self.adjacencyList[u]:
                edges.append((u, vertex.i, vertex.w,vertex.flow))
        return edges

def generate_random_graph(num_vertices, num_edges, max_weight):
    graph = DirectedGraph(num_vertices)
    #print("Creazione del grafo")
    edges_added = 0
    possible_edges = [(u, v) for u in range(num_vertices) for v in range(num_vertices) if u != v]
    random.shuffle(possible_edges)

    for u, v in possible_edges:
        #print("Iterazione" + str(edges_added) + str(num_edges))
        if edges_added < num_edges:
            weight = random.randint(1, max_weight)
            graph.addEdge(u, v, weight)
            edges_added += 1
        else:
            break


    return graph

