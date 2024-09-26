import networkx as nx
import matplotlib.pyplot as plt
from example_gamma2 import *

# Définir les nœuds et les arêtes
nodes = list(range(1, 62))  # Nœuds de 1 à 61
edges = [(1,2), (1,3), (1,5), (2,3), (2,5), (2,12), (3,4), (4,5), (4,7), 
         (4,8), (5,6), (5,17), (5,18), (6,7), (6,17), (6,25), (7,8), (8,25), 
         (9,10), (9,11), (9,48), (10,11), (10,13), (10,46), (11,12), (11,15), 
         (11,46), (12,14), (13,19), (14,15), (14,18), (15,16), (15,46), 
         (16,17), (16,24), (16,46), (17,18), (19,20), (19,23), (20,21), 
         (20,34), (20,51), (20,54), (21,22), (21,35), (22,23), (22,26), 
         (23,46), (24,25), (25,32), (25,42), (25,46), (25,47), (26,27), 
         (27,28), (27,29), (27,35), (28,29), (28,30), (28,31), (29,32), 
         (29,33), (30,31), (30,37), (31,38), (32,33), (33,40), (34,35), 
         (34,55), (35,36), (35,37), (35,55), (36,37), (36,38), (36,57), 
         (37,38), (38,39), (38,40), (38,60), (39,45), (39,60), (40,43), 
         (41,42), (41,43), (42,43), (42,44), (43,45), (44,45), (46,47), 
         (48,49), (48,50), (49,52), (50,51), (52,53), (52,54), (53,54), 
         (53,56), (53,61), (55,56), (55,61), (56,57), (57,58), (58,59), 
         (58,60), (59,60)]

graph2 = Gamma2
graph2.mu = muGam2
graph2.rho = rhoGam2
graph2.phi = phiGam2
graph2.outer = outerGam2
graph2.inner = innerGam2
graph2.outside = outsideGam2
node_colors = [
    'red' if graph2.is_outer(v) 
    else 'green' if graph2.is_inner(v) 
    else 'blue' 
    for v in graph2.V
]


# Créer un graphe
G = nx.Graph()

# Ajouter les nœuds et les arêtes
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Dessiner le graphe
plt.figure(figsize=(12, 12))
nx.draw(G, with_labels=True, node_color=node_colors, node_size=300, font_size=8, font_color='black', edge_color='gray')

# Afficher le graphe
plt.show()
