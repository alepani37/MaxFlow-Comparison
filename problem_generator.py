import random
import graphviz


class Vertex:
    def __init__(self, i, w):
        # numero del vertice finale
        # peso o capacità associata all'arco
        self.i = i
        self.w = w


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


def generate_random_graph(num_vertices, max_weight, edge_probability):
    graph = DirectedGraph(num_vertices)

    for u in range(num_vertices):
        for v in range(num_vertices):
            if u != v:
                if random.random() < edge_probability:  # probabilità di creare l'arco
                    weight = random.randint(1, max_weight)
                    graph.addEdge(u, v, weight)

    return graph