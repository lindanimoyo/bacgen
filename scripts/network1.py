import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

# Load the gene presence/absence matrix
# Example structure:
# Isolate/Plasmid | Gene1 | Gene2 | Gene3 | ...
# Bacteria1       | 1     | 0     | 1     | ...
# Bacteria2       | 0     | 1     | 1     | ...

df = pd.read_csv('amr_gene_presence_matrix.csv')

# Create an empty graph
G = nx.Graph()

# Iterate through each isolate/plasmid
for index, row in df.iterrows():
    # Get genes that are present
    genes_present = [gene for gene, presence in row.items() if presence == 1]
    # Add edges for every pair of co-occurring genes
    for gene1, gene2 in combinations(genes_present, 2):
        if G.has_edge(gene1, gene2):
            G[gene1][gene2]['weight'] += 1
        else:
            G.add_edge(gene1, gene2, weight=1)

# Draw the network
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, seed=42)  # For consistent layout
nx.draw(G, pos, with_labels=True, node_size=700, font_size=10)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Gene Co-occurrence Network')
plt.show()

