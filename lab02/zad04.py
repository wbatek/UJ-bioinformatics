from Bio import SeqIO


def read_fasta(file_path):
    fasta_sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        fasta_sequences[record.id] = str(record.seq)
    return fasta_sequences


def count_gc_content(seq: str):
    c = 0
    for ch in seq:
        if ch in 'CG':
            c += 1
    return (c / len(seq)) * 100.0


data = read_fasta('rosalind_gc.txt')
highest, best_seq = 0, ""

for sequence in data.values():
    current_value = count_gc_content(sequence)
    if current_value > highest:
        highest = current_value
        best_seq = sequence
result_key = next((key for key, value in data.items() if value == best_seq))
print(result_key, highest, sep='\n')
