import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the plasmid-bacteria interaction matrix
# Example structure:
# Plasmid | Bacteria1 | Bacteria2 | Bacteria3 | ...
# Plasmid1| 1         | 0         | 1         | ...
# Plasmid2| 0         | 1         | 1         | ...

df = pd.read_csv('plasmid_bacteria_matrix.csv')

# Create an empty bipartite graph
B = nx.Graph()

# Add nodes with the bipartite attribute
plasmids = df.index.tolist()
bacteria = df.columns.tolist()

B.add_nodes_from(plasmids, bipartite=0)  # Plasmids
B.add_nodes_from(bacteria, bipartite=1)  # Bacterial species

# Add edges
for plasmid in plasmids:
    for bacterium in bacteria:
        if df.loc[plasmid, bacterium] == 1:
            B.add_edge(plasmid, bacterium)

# Draw the bipartite network
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(B, seed=42)
nx.draw(B, pos, with_labels=True, node_size=700, font_size=10)
plt.title('Plasmid-Bacteria Interaction Network')
plt.show()

