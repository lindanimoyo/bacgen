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
![image](https://github.com/user-attachments/assets/e3b3e4f3-d620-4be7-b2a8-2c717313db05)

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

7.__Network analysis__:


8.__Validation:__
To ensure the accuracy and reliability of the pipeline, multiple validation steps were incorporated. The quality of the genome assemblies was assessed using QUAST, evaluating N50, L50, total length, and GC content. AMR gene detection was cross-validated with a ResFinder web service,. Similarly, plasmid and virulence gene detections were cross-validated with other databases or tools, like PlasmidFinder and VFDB web services. Orthologous gene identification was validated by manually inspecting a subset of gene pairs to confirm accuracy.The accuracy of the network analysis was ensured by comparing the constructed network to known plasmid interaction networks and validating the community detection results with known plasmid relationships.

## Results
AMR genes
To investigate antimicrobial resistance (AMR), we employed the abricate tool, which screened the asssemblies against MEGARes. We found a significant prevalence of genes conferring resistance to multiple drug classes. Among aminoglycoside resistance genes, AAC6	-PRIME was present in all isolates, KDPE in 97.73%, ANT3-DPRIME in 16.67%, and APH3-DPRIME and APH6 in 41.67%. For beta-lactam resistance genes, PBP2 was found in 99.62% of the isolates, AMPH in 90.91%, TEM in 35.61%, OXA in 17.80%, and CTX in 10.98%. Sulfonamide resistance genes SULII and SULI were detected in 36.74% and 37.12% of the isolates, respectively, while SULIII was present in 7.95%.

The tetracycline resistance gene TETA was found in 26.89% of the isolates, while TETC was detected in only 0.76%. Among phenicol resistance genes, CATA was present in 34.85% of the isolates and CMLA in 0.38%. The trimethoprim resistance gene DFRA was detected in 37.88% of the isolates. Fluoroquinolone resistance gene QNRB and macrolide resistance gene MEFB were found in 0.38% of the isolates. The bacitracin resistance gene BACA was detected in all isolates, and the fosfomycin resistance gene FOSA was present in 6.44% of the isolates. Multidrug resistance genes MSBA and SDIA were found in all isolates, HNS in 99.62%, and RAMA in 23.48%.Figure 1 is illustrates the percentage presence of the above above AMR genes per serovar group.

In  drug and biocide resistance genes, CPXAR was present in all isolates; MARA and MARR were detected in 99.62% of isolates; and MDTK, BCR, EMRB, EMRA, EMRR, ACRA, ACRB, CRP, EMRD, and YOGII were found in 98% of isolates. The gene QACEDELTA1 was present in 9.85% of isolates, and QACL in 0.38%. Among drug, biocide, and metal resistance genes, MDTA, MDTC, BAER, ACRD, SOXS, GESA, ROBA, and MDTB were found in 99.24% of the isolates, while BAES, GESB, and GESC were detected in 98.11%, 99.62%, and 98.48% of isolates, respectively.Figure 2 illustrates the percentage presence of drug and biocide genes per serovar group

Virulence genes
To investigate virulence genes, we used the abricate tool, which screened the assemblies against the VFDB database to identify genes associated with various pathogenic mechanisms. We found a high prevalence of virulence genes across the isolates. The type III secretion system (T3SS) genes, such as sseJ, sifB, steA, ssaU, ssaT, ssaS, ssaR, ssaQ, ssaP, ssaO, ssaN, ssaV, ssaM, ssaL, ssaK, ssaJ, ssaI, ssaH, ssaG, sseG, and sifA, were present in 100% of the isolates. Additional T3SS genes, including sopE2, steC, ssaE, ssaD, ssaC, spiC/ssaB, sopA, sopD, invH, invF, invG, invE, invA, invB, invC, invI, invJ, spaO, spaP, spaQ, spaR, spaS, sicA, sipB/sspB, sipC/sspC, sipD, sipA/sspA, sicP, prgH, prgI, prgJ, prgK, orgA, orgB, orgC, and mig-14, were detected in more than 99% of the isolates.

Fimbrial adhesion genes csgC, csgA, csgB, csgD, csgE, csgF, csgG, fimF, fimH, fimD, fimC, and fimI were present in 100% of the isolates. Other fimbrial adhesin genes such as lpfE, lpfD, lpfC, lpfB, and lpfA were detected in 91% of the isolates. Non-fimbrial adhesin genes misL, ratB, and sinH were found in 99% of the isolates, while shdA was detected in 20.08% of the isolates.

Intracellularly active toxin genes spvR, spvB, and spvC were detected in 53% of the isolates, and the complement evasion gene rck was found in 53.03% of the isolates. Magnesium uptake genes mgtB and mgtC were present in 99.62% of isolates, while iron uptake-related genes entA and entB were found in 93% of the isolates, fepG in 97.73%, and fepC in 68.94%. Gifsy-2-associated genes sodCI and grvA were detected in 67.05% and 43.18% of the isolates, respectively. Yersiniabactin biosynthetic protein genes ybtT, ybtU, irp1, and irp2 were present in 7.95% of the isolates.Figure 3 illustrates the percentage presence of virulence genes per serovar group.

Plasmids
To investigate plasmids, we employed the abricate tool, which screened the genomic data against the PlasmidFinder database to identify and categorize the plasmid types present in the isolates.We found varied amounts of distinct plasmid types in our dataset. The IncFII(S)_1 and IncFIB(S)_1 plasmids were present in 71.36% of the isolates. Col440I_1 plasmid was found in 32.66% of the isolates, while ColRNAI_1 was identified in 21.61%. The IncHI2A_1, RepA_1_pKPC-CAV1321, and IncHI2_1 plasmids were present in 15.08% of the isolates. IncI1_1_Alpha was detected in 12.56% of the isolates, Col8282_1 in 9.05%, and Col440II_1 in 6.0%. The IncFIB(pHCM2)_1_pHCM2 plasmid was found in 4.52% of the isolates, and IncI_Gamma_1 was identified in 3.02%.Other plasmids such as ColpVC_1, IncFIB(K)_1_Kpn3, IncP1_3, IncFII_1, IncFII(pCRY)_1_pCRY, IncI2_1_Delta, IncQ1_1, and IncFIB(pB171)_1_pB171 were each present in 0.5% of the isolates. Figure 4 illustrates the percentage presence of plasmids per serovar group.



Network analysis


## put the photo here 

This image represents a gene co-occurrence network, which is a visual representation of the relationships between different genes based on their co-expression patterns. The network consists of nodes (represented by the blue circles) that correspond to individual genes, and the connections between them (represented by the lines) indicate the strength of the co-occurrence relationship between the genes.

Clustering of genes
For example, the genes ESR1, FOXP2, and NOVA appear to form a distinct cluster or module in the network, indicating they are likely co-expressed or involved in related biological processes.
Hub genes:
The gene ACTN seems to be a major hub in the network, with a large number of connections to many other genes. This suggests ACTN may be a key regulator or coordinator of gene expression in this system.
Modularity:
The network exhibits a clear modular structure, with groups of genes like BCR, MDT1, and IDT3 forming tight-knit clusters that are more densely connected internally than to other parts of the network. This modular organization likely reflects distinct functional modules or pathways within the overall gene regulatory system.



## Team_members
Names and affiliations
1. Martin Njau Kamau-Meru - University of Science and Technology, Kenya
2. Senbadejo Tosin - University of Ghana
3. Mohamed S. AboHoussien - School of Medicine, Galala University
4. John Njogu - Karatina University
5. SHAFQAT HUSSAIN - Cuvas bahawalpur
6. ⁠Sabreen A. Abo Al-Hassan - Badr un Assuir University
7. Aza-Gnandji Marilyne - Institut de recherche en santé de surveillance épidémiologique et de formation (IRESSEF)  
8. Adejumobi A. Olawale - Redeemer’s University
9. ⁠Davis Kuchaka - Kilimanjaro Clinical Research Institute, Kilimanjaro, Tanzania.
10. Lindani Moyo - National University of Science and Technology, Zimbabwe
11. Abdulkadir I. Abdulkadir - Bayero University Kano, Nigeria
12. Mamadou D. COULIBALY  -   University Clinical Research Center - Mali
13. Kadmiel Adjetey - University of Cape Coast, Ghana
14. ⁠Reem M. SALLAM - Galala University and AinShams University, Egypt
