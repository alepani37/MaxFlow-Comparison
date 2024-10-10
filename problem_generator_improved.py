import random
import networkx as nx

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



    def removeEdge(self, u, v):
        for j in self.adjacencyList[u]:
            if j.i == v:
                self.adjacencyList[u].remove(j)
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


def check_no_reverse_edges(edge_list):
    # Crea un insieme di coppie per evitare duplicati e accessi veloci
    edge_set = set(edge_list)

    # Itera su ogni coppia nell'elenco
    for u, v in edge_list:
        # Controlla se esiste la coppia inversa (v, u) nell'insieme
        if (v, u) in edge_set:
            return False  # Se la coppia inversa esiste, restituisce False
    return True  # Se non sono state trovate coppie inverse, restituisce True

def generate_random_graph(num_vertices, num_edges, max_weight):

    graph = DirectedGraph(num_vertices)
    #print("Creazione del grafo")
    edges_added = 0
    possible_edges = []
    while len(possible_edges) < num_edges:
        u = random.randint(0, num_vertices - 1)  # Seleziona un vertice di partenza
        v = random.randint(0, num_vertices - 1)  # Seleziona un vertice di destinazione

        # Verifica che u != v (nessun ciclo) e che l'arco (u, v) non sia già presente
        if u != v and (u, v) not in possible_edges and (v, u) not in possible_edges:
            possible_edges.append((u, v))

    if not check_no_reverse_edges(possible_edges):
        print("errore")
        return None,False
    random.shuffle(possible_edges)

    for u, v in possible_edges:
        #print("Iterazione" + str(edges_added) + str(num_edges))
        if edges_added < num_edges:
            weight = random.randint(1, max_weight)
            graph.addEdge(u, v, weight)
            edges_added += 1
        else:
            break


    return graph,True

def generate_random(num_vertices, num_edges, max_weight):
    graph = DirectedGraph(num_vertices)
    altro_grafo = nx.DiGraph()
    # print("Creazione del grafo")
    edges_added = 0
    possible_edges = []
    while len(possible_edges) < num_edges:
        u = random.randint(0, num_vertices - 1)  # Seleziona un vertice di partenza
        v = random.randint(0, num_vertices - 1)  # Seleziona un vertice di destinazione

        # Verifica che u != v (nessun ciclo) e che l'arco (u, v) non sia già presente
        if u != v and (u, v) not in possible_edges and (v,u) not in possible_edges:
            possible_edges.append((u, v))
    random.shuffle(possible_edges)

    for u, v in possible_edges:
        # print("Iterazione" + str(edges_added) + str(num_edges))
        if edges_added < num_edges:
            weight = random.randint(1, max_weight)
            graph.addEdge(u, v, weight)
            altro_grafo.add_edge(u, v, capacity=weight)
            edges_added += 1
        else:
            break

    return graph,altro_grafo
