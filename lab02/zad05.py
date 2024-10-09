from Bio import SeqIO


def read_fasta(file_path):
    fasta_sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        fasta_sequences[record.id] = str(record.seq)
    return fasta_sequences


data = read_fasta('rosalind_grph.txt')
k = 3

for name, sequence in data.items():
    for name2, sequence2 in data.items():
        if name == name2:
            continue
        if sequence[len(sequence) - k::] == sequence2[:k]:
            print(name, name2, end='\n')

