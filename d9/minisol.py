import sys

total = 0

for line in map(
        lambda line: [int(l) for l in line.split()], 
        open(sys.argv[1], 'r').read().split('\n') ):
    while sum(line) != 0:
        total += line[-1]
        line = [line[i] - line[i-1] for i in range(1, len(line))]

print(total)
