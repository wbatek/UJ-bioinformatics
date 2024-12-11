import random
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord


def generate_random_fragments(output_file, sequence, fragment_length=200, coverage=5):
    records = []
    seq_length = len(sequence)

    for i in range(int(coverage * seq_length / fragment_length)):
        start = random.randint(0, seq_length - fragment_length)
        fragment = sequence[start:start + fragment_length]
        record = SeqRecord(
            Seq(fragment),
            id=f"fragment_{i + 1}",
            description=f"Random fragment {i + 1}"
        )
        records.append(record)

    with open(output_file, "w") as fasta_file:
        SeqIO.write(records, fasta_file, "fasta")


def find_max_overlap(seq1, seq2):
    max_len = 0
    merged_seq = None

    for i in range(len(seq1)):
        if seq2.startswith(seq1[i:]):
            overlap_len = len(seq1) - i
            if overlap_len > max_len:
                max_len = overlap_len
                merged_seq = seq1 + seq2[overlap_len:]

    for i in range(len(seq2)):
        if seq1.startswith(seq2[i:]):
            overlap_len = len(seq2) - i
            if overlap_len > max_len:
                max_len = overlap_len
                merged_seq = seq2 + seq1[overlap_len:]

    return max_len, merged_seq


def sequence_assembly(input_file):
    fragments = [str(record.seq) for record in SeqIO.parse(input_file, "fasta")]
    contig_count = 1

    while len(fragments) > contig_count:
        max_len = 0
        merged_sequence = None
        best_pair = (None, None)

        for i in range(len(fragments)):
            for j in range(len(fragments)):
                if i != j:
                    overlap_len, merged_seq = find_max_overlap(fragments[i], fragments[j])
                    if overlap_len > max_len:
                        max_len = overlap_len
                        merged_sequence = merged_seq
                        best_pair = (i, j)

        if best_pair == (None, None):
            contig_count += 1
        else:
            i, j = best_pair
            fragments[i] = merged_sequence
            del fragments[j]

    return fragments


# nie wiem, czy dobrze zrozumialem tresc, ale skrocilem plik z chromosomem Y u człowieka do 10000 nukleotydów.
sequence = str(next(SeqIO.parse('data_shorter.fa', 'fasta')).seq)
output_file = "fragments_biopython.fasta"

generate_random_fragments(output_file, sequence)

result = sequence_assembly(output_file)
# sprawdzenie, czy zwrocony został cały input
if len(result) == 1:
    print(result[0] == sequence)
# dlugosc wyniku
print(sum(len(c) for c in result))
# wypisanie wszystkich otrzymanych contigów
print(result)
