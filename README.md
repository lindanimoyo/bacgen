# Bacgen
Bacgen is an advanced pipeline designed for profiling of antimicrobial resistance and network analysis in bacterial genomes. The pipeline integrates bioinformatics tools to automate quality control, genome assembly, AMR gene detection via MEGAres, plasmid detection via PlasmidFinder, and virulence gene identification using VFDB. We then perform Orthologous gene identification between plasmids  BLASTp searches and UCLUST, followed by network construction using the R igraph library. Community detection algorithms are applied to elucidate functional relationships within detected gene clusters.

Bacgen offers a reproducible framework for researchers and clinicians to analyze bacterial whole genome data. This pipeline hopes to advance our understanding of bacterial resistance profiles and microbial pathogenesis.

![methodology_flowchart_bright](https://github.com/user-attachments/assets/028c61ee-3e79-468a-8c5b-8c8a5ce415af)

