from Bio import SeqIO
from Bio.Align import substitution_matrices
from Bio import pairwise2

OPEN_GAP_PEN = 11
EXTEND_GAP_PEN = 1
blosum62 = substitution_matrices.load("BLOSUM62")


def read_fasta(file):
    sequences = []
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(record.seq)
    return sequences


sequences = read_fasta("zad04_in.txt")
alignments = pairwise2.align.localds(sequences[0], sequences[1], blosum62, -OPEN_GAP_PEN, -EXTEND_GAP_PEN)
print(int(alignments[0].score))
print(alignments[0].seqA[alignments[0].start:alignments[0].end].replace("-", ""))
print(alignments[0].seqB[alignments[0].start:alignments[0].end].replace("-", ""))
