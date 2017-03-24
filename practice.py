# Starting from scratch...
import networkx as nx

# Create empty Graph
#By definition, a Graph is a collection of nodes (vertices) along with identified pairs of nodes (called edges, links, etc)
G=nx.Graph()

# Add one node
G.add_node(1)
# Add list of nodes
G.add_nodes_from([2,3])
# Add a bunch of nodes 
H=nx.path_graph(10)
G.add_nodes_from(H)
G.add_node(H)

# Add one edge
G.add_edge(1,2)
e=(2,3)
G.add_edge(*e) # unpack edge tuple*
# Add list of edges
G.add_edges_from([(1,2),(1,3)])
# Add a bunch of edges
G.add_edges_from(H.edges())

# How many nodes?
# print G.number_of_nodes()
# print G.nodes()
# How many edges?
# print G.number_of_edges()
# print G.edges()
# Remove all
G.clear()

# Undirected Graph with Weights
FG=nx.Graph()
FG.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,1.2),(3,4,0.375)])
for n,nbrs in FG.adjacency_iter():
	for nbr,eattr in nbrs.items():
		data=eattr['weight']
		print('(%d, %d, %.3f)' % (n,nbr,data))

# Add graph attributes
# G = nx.Graph(day="Friday")
# print G.graph

# # Degree values 
# sorted(nx.degree(G).values())

# # Clustering
# nx.clustering(G)

# # Drawing Graphs
# import matplotlib.pyplot as plt
# nx.draw(G)
# nx.draw_random(G)
# nx.draw_circular(G)
# nx.draw_spectral(G)
# plt.show()
# nx.draw(G)
# plt.savefig("path.png")
