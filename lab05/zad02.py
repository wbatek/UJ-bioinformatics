import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Align import substitution_matrices
from Bio import pairwise2

OPEN_GAP_PEN = 5
EXTEND_GAP_PEN = 0

blosum62 = substitution_matrices.load("BLOSUM62")


def read_fasta(file):
    sequences = []
    for record in SeqIO.parse(file, "fasta"):
        sequences.append(record.seq)
    return sequences


sequences = read_fasta("zad02_in.txt")
alignments = pairwise2.align.globalds(sequences[0], sequences[1], blosum62, -OPEN_GAP_PEN, EXTEND_GAP_PEN)
print(int(alignments[0].score))
