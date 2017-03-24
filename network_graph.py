# Create network graph from edges data 
import networkx as nx
import pandas as pd
import numpy as np


df = pd.read_csv('C:/Users/Sean Ankenbruck/Desktop/socialmediadata-beeradvocate/code/edge_list.csv')

df= pd.DataFrame(df, columns=['Source','Target','Weight'])
df.Weight = df.Weight.astype(int)

# Remove Zero Values
df = df[df.Weight != 0]


data = df.as_matrix()


# Undirected Graph with Weights
FG=nx.Graph()
FG.add_weighted_edges_from(data)
for n,nbrs in FG.adjacency_iter():
	for nbr,eattr in nbrs.items():
		data=eattr['weight']
		if data>1: print('(%s, %s, %.3f)' % (n,nbr,data))


# Now, how to graph? 
import matplotlib.pyplot as plt 
nx.draw_random(FG)
plt.savefig("network.png")
plt.show()
