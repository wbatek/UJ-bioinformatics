import sys

data = sys.stdin.read().strip()

for i in ['A', 'C', 'G', 'T']:
    print(data.count(i), end=' ')
