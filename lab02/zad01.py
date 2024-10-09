import sys

data = sys.stdin.read().strip().split('\n')
hamming = 0
for i in range(len(data[0])):
    if data[0][i] != data[1][i]:
        hamming += 1
print(hamming)