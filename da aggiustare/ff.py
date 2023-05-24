# Ford-Fulkerson algorith in Python

from collections import defaultdict


class Graph:

    def __init__(self, graph):
        self.graph = graph
        self. ROW = len(graph)


    # Using BFS as a searching algorithm 
    def searching_algo_BFS(self, s, t, parent):

        visited = [False] * (self.ROW)
        queue = []

        queue.append(s)
        visited[s] = True

        while queue:

            u = queue.pop(0)

            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    # Applying fordfulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * (self.ROW)
        max_flow = 0

        while self.searching_algo_BFS(source, sink, parent):

            path_flow = float("Inf")
            s = sink
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Adding the path flows
            max_flow += path_flow

            # Updating the residual values of edges
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

#          #S  A  B  C  D  T
# graph = [[0, 8, 0, 0, 3, 0],
#          [0, 0, 9, 0, 0, 0],
#          [0, 0, 0, 0, 7, 2],
#          [0, 0, 0, 0, 0, 5],
#          [0, 0, 7, 4, 0, 0],
#          [0, 0, 0, 0, 0, 0]]

         #1  2  3  4  5  6  7
# graph = [[0, 7, 7, 0, 0, 0, 0],
#          [0, 0, 3, 2, 3, 0, 0],
#          [0, 0, 0, 0, 0, 2, 0],
#          [0, 0, 4, 0, 1, 4, 3],
#          [0, 0, 0, 0, 0, 0, 8],
#          [0, 0, 0, 0, 0, 0, 9],
#          [0, 0, 0, 0, 0, 0, 0]]

#          #1  2  3  4  5  6  7
# graph = [[0, 6, 6, 0, 0, 0, 0],
#          [0, 0, 1, 3, 3, 0, 0],
#          [0, 0, 0, 0, 7, 0, 0],
#          [0, 0, 0, 0, 1, 0, 1],
#          [0, 0, 0, 0, 0, 5, 4],
#          [0, 0, 0, 0, 0, 0, 4],
#          [0, 0, 0, 0, 0, 0, 0]]

         #1  2  3  4  5  6  7
graph = [[0, 6, 6, 0, 0, 0, 0],
         [6, 0, 1, 3, 3, 0, 0],
         [6, 1, 0, 0, 7, 0, 0],
         [0, 0, 0, 0, 1, 0, 1],
         [0, 0, 7, 0, 0, 5, 4],
         [0, 0, 0, 0, 0, 0, 4],
         [0, 0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 6

print("Max Flow: %d " % g.ford_fulkerson(source, sink))