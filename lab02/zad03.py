from Bio import SeqIO


def read_fasta(file_path):
    fasta_sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        fasta_sequences[record.id] = str(record.seq)
    return fasta_sequences


data = read_fasta('rosalind_tran.txt')
transitions = ['AG', 'GA', 'CT', 'TC']
transversions = ['AC', 'CA', 'GT', 'TG', 'AT', 'TA', 'CG', 'GC']
x, y = 0, 0
sequences = list(data.values())

for i in range(len(sequences[0])):
    current = sequences[0][i] + sequences[1][i]
    if current in transitions:
        x += 1
    elif current in transversions:
        y += 1
print(x / y)
