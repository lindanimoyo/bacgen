# Bacgen
## Table of Contents
- [Introduction](#Introduction)
- [Objectives](#Objectives)
- [Workflow](#Workflow)
- [Methods](#Methods)
- [Team_members](#Team_members)

## Introduction
Bacgen is an advanced pipeline designed for antimicrobial resistance profiling and network analysis in bacterial genomes. The pipeline integrates bioinformatics tools to automate quality control, genome assembly, AMR gene detection via MEGAres, plasmid detection via PlasmidFinder, and virulence gene identification using VFDB. It then performs Orthologous gene identification between plasmids  BLASTp searches and UCLUST, followed by network construction using the R igraph library.It then uses community detection algorithms to elucidate functional relationships within detected gene clusters.
Bacgen offers a reproducible framework for researchers and clinicians to analyze bacterial whole genome data. This pipeline hopes to advance our understanding of bacterial resistance profiles and microbial pathogenesis.

## Objectives
1. __Automate AMR profiling and network analysis__: Develop a streamlined pipeline to automate detection and profiling of antimicrobial resistance genes (AMR),plasmids,virulence Genes and construction gene interaction networks.
2. __Validation__: Validate Bacgen across diverse bacterial genomes.

## Workflow
![methodology_flowchart_bright](https://github.com/user-attachments/assets/028c61ee-3e79-468a-8c5b-8c8a5ce415af)

## Methods
1.__Raw sequence quality control__:
The quality of raw sequencing reads was assessed using FastQC to ensure high-quality data for downstream analyses. Raw reads in FASTQ format were processed, and quality reports were generated.

2.__Trimming and filtering__:
Reads were trimmed and filtered using Trimmomatic to remove low-quality bases and adapter sequences. The trimming process involved removing low-quality bases from the ends of reads and discarding reads shorter than 36 bases.

3.__Genome assembly__:
High-quality reads were assembled into contigs using Unicycler. The assembly process produced contigs that were used in subsequent analyses.

4.__AMR gene detection__:
Antimicrobial resistance (AMR) genes were identified using Abricate with MEGAres database. Abricate scans genomic assemblies for known resistance genes and generates a comprehensive report detailing the detected AMR genes.

5.__Plasmid detection__:
Plasmids within the assembled genomes were detected using the PlasmidFinder database in Abricate. This process involved scanning the assembled contigs for plasmid sequences and reporting the identified plasmid types.

6.__Virulence gene detection__:
Virulence genes were identified using the VFDB database in Abricate. This step involved scanning the genomic assemblies for known virulence factors and generating a report of the detected virulence genes.

7.__BLASTp searches:__
To identify orthologous genes between plasmids, BLASTp searches were performed with specific parameters to ensure high-confidence hits. Hits with e-values less than 1E-10, cover ratios more than 90%, and length differences within the range of 0.9 < query/subject < 1.1 were retained for further analysis.

8.__Filtering BLASTp Results:__
BLASTp results were filtered to include only hits that met the criteria of e-values less than 1E-10, cover ratios more than 90%, and length differences within the range of 0.9 < query/subject < 1.1. This filtering ensured that only high-confidence orthologous genes were considered.

9.__Shared protein searches using uCLUST:__
The UCLUST program was used to identify shared proteins between plasmids. Sequences were sorted by length and clustered with parameters that ensured a minimum sequence length similarity of 0.9, query and target coverages of 0.9, and length differences within the range of 0.9 < query/subject < 1.1.

10.__Network analysis input:__
The input for network analysis consisted of the filtered BLASTp results and UCLUST results. These inputs provided the basis for constructing a graph where nodes represented plasmids and edges represented shared genes, with edge weights corresponding to the number of shared genes.

11.__Network construction and analysis:__
Network analyses were performed using the R igraph library (v1.2.6). Filtered BLASTp results were used to construct a graph. The weight of each edge was defined by the number of shared genes. Community detection was performed using multiple algorithms, including edge.betweenness.community, multilevel.community, label.propagation.community, infomap.community, walktrap.community, and fastgreedy.community. The detected communities were saved to CSV files for further analysis.

12.__Validation:__
To ensure the accuracy and reliability of the pipeline, multiple validation steps were incorporated. The quality of the genome assemblies was assessed using QUAST, evaluating N50, L50, total length, and GC content. AMR gene detection was cross-validated with a ResFinder web service,. Similarly, plasmid and virulence gene detections were cross-validated with other databases or tools, like PlasmidFinder and VFDB web services. Orthologous gene identification was validated by manually inspecting a subset of gene pairs to confirm accuracy.The accuracy of the network analysis was ensured by comparing the constructed network to known plasmid interaction networks and validating the community detection results with known plasmid relationships.

## Team members
Names and affiliations
1. Martin Njau Kamau-Meru - University of Science and Technology, Kenya
2. Senbadejo Tosin - University of Ghana
3. Mohamed S. AboHoussien - School of Medicine, Galala University
4. John Njogu - Karatina University
5. SHAFQAT HUSSAIN - Cuvas bahawalpur
6. ⁠Sabreen A. Abo Al-Hassan - Badr un Assuir University
7. Aza-Gnandji Marilyne - Institut de recherche en santé de surveillance épidémiologique et de formation (IRESSEF)  
8. Adejumobi A. Olawale - Redeemer’s University
9. ⁠Davis Kuchaka - Kilimanjaro Clinical Research Institute, Kilimanjaro, Tanzania. The Nelson Mandela African Institution of Science and Technology, Arusha, Tanzania
10. Lindani Moyo - National University of Science and Technology, Zimbabwe
11. Abdulkadir I. Abdulkadir - Bayero University Kano, Nigeria
12. Mamadou D. COULIBALY  -   University Clinical Research Center - Mali
13. Kadmiel Adjetey - University of Cape Coast, Ghana
14. ⁠Reem M. SALLAM - Galala University and AinShams University, Egypt
