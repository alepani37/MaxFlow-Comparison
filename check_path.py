from problem_generator_improved import DirectedGraph

def isReachable(graph,s,t):

    visited = [False] * graph.vertices
    queue = []

    queue.append(s)
    visited[s] = True
    while queue:

        vertex = queue.pop(0)
        if vertex == t:
            return True

        for i in graph.adjacencyList[vertex]:
            if visited[i.i] == False:
                visited[i.i] = True
                queue.append(i.i)
    return False