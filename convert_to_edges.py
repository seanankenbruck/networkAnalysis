# Convert adjacency matrix to list of edges and nodes 
import pandas as pd
import numpy as np
import networkx as nx
import csv

matrix = pd.read_csv("C:/Users/Sean Ankenbruck/Desktop/socialmediadata-beeradvocate/code/beer_style_adjacency.csv")

def adj_to_list(input_filename,output_filename,delimiter):
	'''Takes the adjacency matrix on file input_filename into a list of edges and saves it into output_filename'''
	A=pd.read_csv(input_filename,delimiter=delimiter,index_col=0)
	List=[('Source','Target','Weight')]
	for source in A.index.values:
	    for target in A.index.values:
	        List.append((target,source,A[source][target]))
	with open(output_filename, "wb") as f:
	    writer = csv.writer(f)
	    writer.writerows(List)
	return List

List=adj_to_list('beer_style_adjacency.csv','edge_list.csv',',')