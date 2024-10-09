from Bio import SeqIO


def read_fasta(file_path):
    fasta_sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        fasta_sequences[record.id] = str(record.seq)
    return fasta_sequences


complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}


def get_complement(sequence):
    return ''.join(complements.get(base, base) for base in sequence[::-1])


codon_table = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
    'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'TAT': 'Y', 'TAC': 'Y', 'TAA': 'Stop', 'TAG': 'Stop',
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'TGT': 'C', 'TGC': 'C', 'TGA': 'Stop', 'TGG': 'W',
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}


def get_all_frames(sequence):
    proteins = set()
    for offset in range(0, len(sequence) - 2):
        current = ''
        started = False
        for i in range(offset, len(sequence) - 2, 3):
            codon = sequence[i:i + 3]
            amino_acid = codon_table[codon]
            if amino_acid == 'Stop':
                if started:
                    proteins.add(current)
                    started = False
                    current = ''

            if amino_acid == 'M':
                started = True
            if started:
                current += amino_acid
    return proteins


data = read_fasta('rosalind_orf.txt')
sequence = list(data.values())[0]
all_proteins = get_all_frames(sequence).union(get_all_frames(get_complement(sequence)))
for protein in all_proteins:
    print(protein)
