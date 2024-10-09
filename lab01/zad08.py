import sys

data = sys.stdin.read().strip()
complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

data = data[::-1]
for i in data:
    print(complements.get(i), end='')
