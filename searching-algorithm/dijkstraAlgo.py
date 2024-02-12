import numpy as np
from collections import deque
import math
import networkx as nx
# array that holds shortest distance from src to every vertex
# n=10
# dist= [math.inf]* 10
# source=0
# dist[source]= 0
# # print(dist[5])
# Q= deque([source])

# while Q

graph= nx.DiGraph()
graph.add_nodes_from(['Abc','B', 'C','D'])
graph.add_edge(7, "llo")
graph.add_edge(88, "B")
edges = [("B", "C", 1.2), ("C", "D", 3.4), ("A", "D", 2.6)]
graph.add_weighted_edges_from(edges)
print(graph.number_of_edges())
print(graph.number_of_nodes())
print(graph.nodes)
print(graph.edges)

import matplotlib.pyplot as plt

pos = nx.spring_layout(graph)  # positions for all nodes
nx.draw(graph, pos, with_labels=True)
edge_labels = nx.get_edge_attributes(graph, "weight")
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

plt.show()
