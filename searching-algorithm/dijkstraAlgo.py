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
graph.add_edge(7, "llo", 0.9)
graph.add_edge(88, "B", 0.6)
edges = [("B", "C", 1.2), ("C", "D", 3.4), ("A", "D", 2.6)]
graph.add_weighted_edges_from(edges)
print(graph.number_of_edges())
print(graph.number_of_nodes())
print(graph.nodes)
print(graph.edges)
