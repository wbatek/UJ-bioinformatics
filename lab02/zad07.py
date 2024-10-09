import sys

data = sys.stdin.read().strip().split('\n')
result = []

for i in range(len(data[0])):
    if data[0][i: i + len(data[1])] == data[1]:
        result.append(i + 1)
for element in result:
    print(element, end=' ')
