import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

def transpose(lines):
    return 

expanded_cols = []
t_lines = [''.join([lines[y][x] for y in range(len(lines))]) for x in range(len(lines[0]))]
for col in range(len(t_lines)):
    if not '#' in t_lines[col]:
        expanded_cols += [col]

expanded_rows = []
for row in range(len(lines)):
    if not '#' in lines[row]:
        expanded_rows += [row]

galaxies = []

for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            galaxies += [(x, y)]

def dist(g1, g2):
    distance = 0
    for i in expanded_rows:
        if min(g1[1], g2[1]) < i < max(g1[1], g2[1]):
            distance += 1
    for i in expanded_cols:
        if min(g1[0], g2[0]) < i < max(g1[0], g2[0]):
            distance += 1

    taxicab = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return taxicab + distance

for g1 in range(len(galaxies)):
    for g2 in range(g1 + 1, len(galaxies)):
        total += dist(galaxies[g1], galaxies[g2])

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')