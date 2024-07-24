# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 12:18:08 2024

@author: mdcoulibaly
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading datasets
megares_df = pd.read_csv(r'path to\all.megares.csv')
plasmid_df = pd.read_csv(r'path to\all.plasmidfinder.csv')
resfind_df = pd.read_csv(r'path to\all.resfinder.csv')
vfdb_df = pd.read_csv(r'path to\all.vfdb.csv')

# Create pivot tables for heatmaps
megares_heatmap_coverage =megares_df.pivot_table(index='GENE', values='%COVERAGE')
plasmid_heatmap_coverage =plasmid_df.pivot_table(index='GENE', values='%COVERAGE')
resfind_heatmap_coverage =resfind_df.pivot_table(index='GENE', values='%COVERAGE')
vfdb_heatmap_coverage =vfdb_df.pivot_table(index='GENE', values='%COVERAGE')

megares_heatmap_identity =megares_df.pivot_table(index='GENE', values='%IDENTITY')
plasmid_heatmap_identity =plasmid_df.pivot_table(index='GENE', values='%IDENTITY')
resfind_heatmap_identity =resfind_df.pivot_table(index='GENE', values='%IDENTITY')
vfdb_heatmap_identity =vfdb_df.pivot_table(index='GENE', values='%IDENTITY')




# Add a category column to each dataset to facilitate concatenation
megares_df['Category'] = 'MEGARES'
plasmid_df['Category'] = 'PLASMID'
resfind_df['Category'] = 'RESFIND'
vfdb_df['Category'] = 'VFDB'

# Combine the Datasets
combined_df = pd.concat([megares_df, plasmid_df, resfind_df,vfdb_df])

# Create a correlation matrix for percentage coverage and percentage identity
correlation_matrix = combined_df.pivot_table(index='GENE', columns='Category', values=['%COVERAGE', '%IDENTITY']).corr()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Heatmap for Percentage Coverage and Percentage Identity')
plt.show()




# Heatmap for megares: Percentage Coverage
plt.figure(figsize=(40, 20))
sns.heatmap(megares_heatmap_coverage, annot=True, cmap='coolwarm')
plt.title('MEGARES: Percentage Coverage')
plt.xlabel('%COVERAGE')
plt.ylabel('GENE')

# Heatmap for PLASMIDE: Percentage Coverage
plt.figure(figsize=(40, 20))
sns.heatmap(plasmid_heatmap_coverage, annot=True, cmap='coolwarm')
plt.title('PLASMIDE: Percentage Coverage')
plt.xlabel('%COVERAGE')
plt.ylabel('GENE')

# Heatmap for Resfind: Percentage Coverage
plt.figure(figsize=(40, 20))
sns.heatmap(resfind_heatmap_coverage, annot=True, cmap='coolwarm')
plt.title('RESFIND: Percentage Coverage')
plt.xlabel('%COVERAGE')
plt.ylabel('GENE')

# Heatmap for VFDB: Percentage Coverage
plt.figure(figsize=(40, 20))
sns.heatmap(vfdb_heatmap_coverage, annot=True, cmap='coolwarm')
plt.title('VFDB: Percentage Coverage')
plt.xlabel('%COVERAGE')
plt.ylabel('GENE')




# Heatmap for MEGARES: Percentage Identity
plt.figure(figsize=(40, 20))
sns.heatmap(megares_heatmap_identity, annot=True, cmap='coolwarm')
plt.title('MEGARES: Percentage Identity')
plt.xlabel('%IDENTITY')
plt.ylabel('GENE')

# Heatmap for PLASMIDE: Percentage Identity
plt.figure(figsize=(40, 20))
sns.heatmap(plasmid_heatmap_identity, annot=True, cmap='coolwarm')
plt.title('PLASMIDE: Percentage Identity')
plt.xlabel('%IDENTITY')
plt.ylabel('GENE')

# Heatmap for RESFIND: Percentage Identity
plt.figure(figsize=(40, 20))
sns.heatmap(resfind_heatmap_identity, annot=True, cmap='coolwarm')
plt.title('RESFIND: Percentage Identity')
plt.xlabel('%IDENTITY')
plt.ylabel('GENE')

# Heatmap for VFDB: Percentage Identity
plt.figure(figsize=(40, 20))
sns.heatmap(vfdb_heatmap_identity, annot=True, cmap='coolwarm')
plt.title('VFDB: Percentage Identity')
plt.xlabel('%IDENTITY')
plt.ylabel('GENE')





# Bar plot for MEGARES: Gene Product Count
plt.figure(figsize=(40, 20))
sns.countplot(data=megares_df, y='PRODUCT', order=megares_df['PRODUCT'].value_counts().index)
plt.title('MEGARES: Gene Product Count')
plt.xlabel('Count')
plt.ylabel('PRODUCT')

# Bar plot for PLASMIDE: Gene Product Count
plt.figure(figsize=(40, 20))
sns.countplot(data=plasmid_df, y='PRODUCT', order=plasmid_df['PRODUCT'].value_counts().index)
plt.title('PLASMIDE: Gene Product Count')
plt.xlabel('Count')
plt.ylabel('PRODUCT')

# Bar plot for RESFIND: Gene Product Count
plt.figure(figsize=(40, 20))
sns.countplot(data=resfind_df, y='PRODUCT', order=resfind_df['PRODUCT'].value_counts().index)
plt.title('RESFIND: Gene Product Count')
plt.xlabel('Count')
plt.ylabel('PRODUCT')

# Bar plot for VFDB: Gene Product Count
plt.figure(figsize=(40, 20))
sns.countplot(data=vfdb_df, y='PRODUCT', order=vfdb_df['PRODUCT'].value_counts().index)
plt.title('VFDB: Gene Product Count')
plt.xlabel('Count')
plt.ylabel('PRODUCT')






# Distribution plot for MEGARES: Percentage Coverage and Identity
plt.figure(figsize=(40, 20))
sns.histplot(megares_df['%COVERAGE'], kde=True, color='blue', label='Coverage')
sns.histplot(megares_df['%IDENTITY'], kde=True, color='red', label='Identity')
plt.title('MEGARES: Distribution of Percentage Coverage and Identity')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.legend()

# Distribution plot for PLASMIDE: Percentage Coverage and Identity
plt.figure(figsize=(40, 20))
sns.histplot(plasmid_df['%COVERAGE'], kde=True, color='blue', label='Coverage')
sns.histplot(plasmid_df['%IDENTITY'], kde=True, color='red', label='Identity')
plt.title('PLASMIDE: Distribution of Percentage Coverage and Identity')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.legend()

# Distribution plot for RESFIND: Percentage Coverage and Identity
plt.figure(figsize=(40, 20))
sns.histplot(resfind_df['%COVERAGE'], kde=True, color='blue', label='Coverage')
sns.histplot(resfind_df['%IDENTITY'], kde=True, color='red', label='Identity')
plt.title('RESFIND: Distribution of Percentage Coverage and Identity')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.legend()

# Distribution plot for VFDB: Percentage Coverage and Identity
plt.figure(figsize=(40, 20))
sns.histplot(vfdb_df['%COVERAGE'], kde=True, color='blue', label='Coverage')
sns.histplot(vfdb_df['%IDENTITY'], kde=True, color='red', label='Identity')
plt.title('VFDB: Distribution of Percentage Coverage and Identity')
plt.xlabel('Percentage')
plt.ylabel('Frequency')
plt.legend()





