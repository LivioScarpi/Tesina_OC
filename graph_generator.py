import networkx as nx
import pickle
import os
import random
import matplotlib.pyplot as plt
import math

def create_graph(n_nodes, n_edges):
    G = nx.gnm_random_graph(n_nodes, n_edges, directed = True) #[0, n_nodes-1] ; s = n_nodes ; t = n_nodes+1

    #code creating G here
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,100)

    G.add_node(n_nodes)
    G.add_node(n_nodes+1)
    
    for i in range(math.floor(n_nodes / 30)):
        j = random.randint(0, n_nodes-1)
        while(G.has_edge(n_nodes, j)):
            j = random.randint(0, n_nodes-1)
        G.add_edge(n_nodes, j, weight=random.randint(0,100))

    for i in range(math.floor(n_nodes / 30)):
        j = random.randint(0, n_nodes-1)
        while(G.has_edge(j, n_nodes+1)):
            j = random.randint(0, n_nodes-1)
        G.add_edge(j, n_nodes+1, weight=random.randint(0,100))

    directory = os.getcwd()
    filename = directory + "/grafi_da_eseguire/graph_V" + str(n_nodes) + "_E" + str(n_edges) + "_weighted.pickle"
    with open(filename, 'wb') as fp: 
        pickle.dump(G, fp)

    # To load the graph from the file:
    # G = pickle.load(open('filename.pickle', 'rb'))
    # print(G.edges)
    # nx.draw(G)
    # plt.show()

def main():
    n_nodes = input("Nodes: ")
    n_edges = input("Edges: ")
    create_graph(int(n_nodes), int(n_edges))

if __name__ == "__main__":
    main()