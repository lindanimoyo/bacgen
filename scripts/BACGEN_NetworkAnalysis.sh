#!/usr/bin/env bash

cd $HOME/OMICS_CODEATHON_BACGEN

# Network Analysis Study using Bioinformatics Tools
# Author: "Marilyne Aza-Gnandji <azagnandji.marilyne@iressef.org>"
#+DATE:[2024-07-22 Lun.]

## Set up directories
WORKDIR=$HOME/OMICS_CODEATHON_BACGEN
DATADIR=$WORKDIR/data
RESULTSDIR=$WORKDIR/results
SCRIPTDIR=$WORKDIR/scripts
mkdir -p $DATADIR $RESULTSDIR $SCRIPTDIR

##System updating and ncbi-blast+ tool installation:it allows blastp availability
sudo apt-get update
sudo apt-get install ncbi-blast+ && sudo apt autoremove

# Step 1: Download test Sequence Data
echo "Downloading sequence data..."
echo -e wget -O $DATADIR/sequences.fasta "http://example.com/sequences.fasta"

#Download the nr database from ncbi
echo -e wget ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nr.gz | tar -zxvf nr.gz

#Index the database:am not sure it is necessary ##Yes it's make the search faster against the protein db 
#echo -e makeblastdb -in nr -dbtype prot

# Step 2: Perform Sequence Alignment using BLAST
echo "Running BLAST for sequence alignment..."
echo -e blastp -query $DATADIR/sequences.fasta -db nr -out $RESULTSDIR/blast_results.txt -evalue 0.001 -outfmt 6 -num_threads 4

# Step 3: Parse BLAST results and create interaction network
echo "Parsing BLAST results..."
echo -e python3 $SCRIPTDIR/parse_blast_results.py $RESULTSDIR/blast_results.txt $RESULTSDIR/network_edges.csv

#steps to install the development version of cytoscape3
git clone https://github.com/cytoscape/cytoscape.git
cd cytoscape
./cy.sh init
cd cytoscape
mvn -fae install -U -Dmaven.test.skip=true
./gui-distribution/assembly/target/cytoscape/cytoscape.sh

# Step 4: Prepare data for Cytoscape
echo "Preparing data for Cytoscape..."
echo -e python3 $SCRIPTDIR/prepare_cytoscape_data.py $RESULTSDIR/network_edges.csv $RESULTSDIR/cytoscape_network.txt

# Step 5: Visualize Network in Cytoscape
echo "Visualizing network in Cytoscape..."
echo -e cytoscape.sh -N $RESULTSDIR/cytoscape_network.txt

#last file named cytoscape_network.txt creation verification to test if the pipeline seems to work till the end
# we can check this file creation like this:
echo -e sudo find / -type f -name "$RESULTSDIR/cytoscape_network.txt"

echo "Network analysis completed successfully."


##Test with UCLUST==Shared Protein Searches using UCLUST

