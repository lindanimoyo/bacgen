# Bacgen
## Table of Contents
- [Introduction](## Introduction)
- [Objectives](## Objectives)
- [Workflow](## Workflow)
- [Methods](## Methods)

## Introduction
Bacgen is an advanced pipeline designed for antimicrobial resistance profiling and network analysis in bacterial genomes. The pipeline integrates bioinformatics tools to automate quality control, genome assembly, AMR gene detection via MEGAres, plasmid detection via PlasmidFinder, and virulence gene identification using VFDB. We then perform Orthologous gene identification between plasmids  BLASTp searches and UCLUST, followed by network construction using the R igraph library. Community detection algorithms are applied to elucidate functional relationships within detected gene clusters.
Bacgen offers a reproducible framework for researchers and clinicians to analyze bacterial whole genome data. This pipeline hopes to advance our understanding of bacterial resistance profiles and microbial pathogenesis.

## Objectives
1. __Automate AMR Profiling and Network Analysis__: Develop a streamlined pipeline to automate detection and profiling of antimicrobial resistance genes (AMR),plasmids,virulence Genes and construction gene interaction networks.
2. __Validation__: Validate Bacgen across diverse bacterial genomes.

## Workflow
![methodology_flowchart_bright](https://github.com/user-attachments/assets/028c61ee-3e79-468a-8c5b-8c8a5ce415af)

## Methods
1. __Quality Control and Genome Assembly__
Raw Sequence Quality Control:
The quality of raw sequencing reads was assessed using FastQC to ensure high-quality data for downstream analyses. Raw reads in FASTQ format were processed, and quality reports were generated.

Trimming and Filtering:
Reads were trimmed and filtered using Trimmomatic to remove low-quality bases and adapter sequences. The trimming process involved removing low-quality bases from the ends of reads and discarding reads shorter than 36 bases.

Genome Assembly:
High-quality reads were assembled into contigs using Unicycler. The assembly process produced contigs that were used in subsequent analyses.

2. __AMR, Plasmid, and Virulence Gene Detection__
AMR Gene Detection:
Antimicrobial resistance (AMR) genes were identified using Abricate with MEGAres database. Abricate scans genomic assemblies for known resistance genes and generates a comprehensive report detailing the detected AMR genes.

Plasmid Detection:
Plasmids within the assembled genomes were detected using the PlasmidFinder database in Abricate. This process involved scanning the assembled contigs for plasmid sequences and reporting the identified plasmid types.

Virulence Gene Detection:
Virulence genes were identified using the VFDB database in Abricate. This step involved scanning the genomic assemblies for known virulence factors and generating a report of the detected virulence genes.

3.__Orthologous Gene Identification__
BLASTp Searches:
To identify orthologous genes between plasmids, BLASTp searches were performed with specific parameters to ensure high-confidence hits. Hits with e-values less than 1E-10, cover ratios more than 90%, and length differences within the range of 0.9 < query/subject < 1.1 were retained for further analysis.

Filtering BLASTp Results:
BLASTp results were filtered to include only hits that met the criteria of e-values less than 1E-10, cover ratios more than 90%, and length differences within the range of 0.9 < query/subject < 1.1. This filtering ensured that only high-confidence orthologous genes were considered.

Shared Protein Searches using UCLUST:
The UCLUST program was used to identify shared proteins between plasmids. Sequences were sorted by length and clustered with parameters that ensured a minimum sequence length similarity of 0.9, query and target coverages of 0.9, and length differences within the range of 0.9 < query/subject < 1.1.

4. __Network Analysis__
Input for Network Analysis:
The input for network analysis consisted of the filtered BLASTp results and UCLUST results. These inputs provided the basis for constructing a graph where nodes represented plasmids and edges represented shared genes, with edge weights corresponding to the number of shared genes.

Network Construction and Analysis:
Network analyses were performed using the R igraph library (v1.2.6). Filtered BLASTp results were used to construct a graph. The weight of each edge was defined by the number of shared genes. Community detection was performed using multiple algorithms, including edge.betweenness.community, multilevel.community, label.propagation.community, infomap.community, walktrap.community, and fastgreedy.community. The detected communities were saved to CSV files for further analysis.

