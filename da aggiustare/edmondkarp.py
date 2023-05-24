#Edmonds-Karp Algorithm
def max_flow(C, s, t):
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)]
        path = bfs(C, F, s, t)
      #  print path
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            path = bfs(C, F, s, t)
        return sum(F[s][i] for i in range(n))

#find path by using BFS
def bfs(C, F, s, t):
        print("cerco un nuovo path")

        queue = [s]
        paths = {s:[]}
        if s == t:
            return paths[s]
        while queue: 
            u = queue.pop(0)
            for v in range(len(C)):
                    if(C[u][v]-F[u][v]>0) and v not in paths:
                        paths[v] = paths[u]+[(u,v)]
                        #print(paths)

                        last_key = list(paths)[-1]
                        #print(last_key)  # 👉️ country

                        print(paths[last_key]) # 👉️ Belgium
                        print("\n")
                        if v == t:
                            return paths[v]
                        queue.append(v)
        return None
    
# make a capacity graph
# node   s   o   p   q   r   t
# C = [[ 0, 3, 3, 0, 0, 0 ],  # s
#      [ 0, 0, 2, 3, 0, 0 ],  # o
#      [ 0, 0, 0, 0, 2, 0 ],  # p
#      [ 0, 0, 0, 0, 4, 2 ],  # q
#      [ 0, 0, 0, 0, 0, 2 ],  # r
#      [ 0, 0, 0, 0, 0, 3 ]]  # t

# node 1  2  3  4   5  6  7  8
C = [[ 0, 6, 4, 10, 0, 0, 0, 0], # 1
     [ 0, 0, 2, 0,  6, 0, 0, 0 ], # 2
     [ 0, 0, 0, 0,  5, 2, 0, 1 ], # 3
     [ 0, 0, 3, 0,  0, 4, 0, 0 ], # 4
     [ 0, 0, 0, 0,  0, 0, 9, 0 ], # 5
     [ 0, 0, 0, 0,  0, 0, 9, 0 ], # 6
     [ 0, 0, 0, 0,  0, 0, 0, 0 ], # 7
     [ 0, 0, 0, 0,  3, 3, 0, 0 ]] # 8

# C = [[ 0, 6, 8, 0,  0, 0, 0], # 1
#      [ 0, 0, 0, 10, 0, 0, 0], # 2
#      [ 0, 3, 0, 4,  4, 0, 0], # 3
#      [ 0, 0, 0, 0,  1, 3, 10], # 4
#      [ 0, 0, 0, 0,  0, 0, 3], # 5
#      [ 0, 13, 0, 0,  0, 0, 2], # 6
#      [ 0, 0, 0, 0,  0, 0, 0]] # 7

source = 0  # LA SORGENTE E' 1
sink = 6    # LA DESTINAZIONE E' 7
max_flow_value = max_flow(C, source, sink)
print("Edmonds-Karp algorithm")
print("max_flow_value is: ", max_flow_value)
