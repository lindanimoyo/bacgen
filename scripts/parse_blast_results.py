import sys

def parse_blast_results(blast_file, output_file):
    with open(blast_file, 'r') as bf, open(output_file, 'w') as of:
        of.write("source\ttarget\tscore\n")
        for line in bf:
            parts = line.strip().split('\t')
            source = parts[0]
            target = parts[1]
            score = parts[11]
            of.write(f"{source}\t{target}\t{score}\n")

if __name__ == "__main__":
    parse_blast_results(sys.argv[1], sys.argv[2])
