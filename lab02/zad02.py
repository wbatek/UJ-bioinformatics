from Bio import SeqIO


def read_fasta(file_path):
    fasta_sequences = {}
    for record in SeqIO.parse(file_path, "fasta"):
        fasta_sequences[record.id] = str(record.seq)
    return fasta_sequences


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0]) - i + 1):
                if j > len(substr) and is_substring(data[0][i:i + j], data):
                    substr = data[0][i:i + j]
    return substr


def is_substring(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


data = read_fasta('rosalind_lcsm.txt')
print(long_substr(list(data.values())))
