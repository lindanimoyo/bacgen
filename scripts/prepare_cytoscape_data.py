import sys

def prepare_cytoscape_data(network_file, output_file):
    with open(network_file, 'r') as nf, open(output_file, 'w') as of:
        of.write("source\ttarget\ttype\n")
        next(nf)  # Skip header
        for line in nf:
            parts = line.strip().split('\t')
            source = parts[0]
            target = parts[1]
            of.write(f"{source}\t{target}\t\"interacts_with\"\n")

if __name__ == "__main__":
    prepare_cytoscape_data(sys.argv[1], sys.argv[2])
