import networkx as nx
import pickle
import os
import random

def create_graph(n_nodes, n_edges):
    G = nx.dense_gnm_random_graph(n_nodes, n_edges)

    #code creating G here
    for (u,v,w) in G.edges(data=True):
        w['weight'] = random.randint(0,100)

    directory = os.getcwd()
    filename = directory + "/grafi/graph_V" + str(n_nodes) + "_E" + str(n_edges) + "_weighted.pickle"
    with open(filename, 'wb') as fp: 
        pickle.dump(G, fp)

    # To load the graph from the file:
    # G = pickle.load(open('filename.pickle', 'rb'))

def main():
    n_nodes = input("Nodes: ")
    n_edges = input("Edges: ")
    create_graph(int(n_nodes), int(n_edges))

if __name__ == "__main__":
    main()