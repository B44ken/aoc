import sys, re
if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')

pipes = {
    'S': [[1, 0], [-1, 0], [0, 1], [0, -1]],
    '.': [],
    '|': [[0, -1], [0, 1]],
    '-': [[1, 0], [-1, 0]],
    'L': [[1, 0], [0, 1]],
    'J': [[1, 0], [0, -1]],
    '7': [[1, 0], [0, 1]],
    'F': [[1, 0], [0, -1]]
}

currents = []

pad = ['.' * (len(lines[0]) + 2)]

lines = pad + ['.' + line + '.' for line in lines] + pad
passed = [ [-1 for i in l] for l in lines ]

total = 0
for l in range(len(lines)):
    if 'S' in lines[l]:
        currents += [[lines[l].index('S'), l]]


def debug_print(lines, passed):
    for l in passed:
        for c in l:
            print(str(c).ljust(3), end=' ')
        print()

    for l in lines:
        for c in l:
            print(c + '   ', end='')
        print()

def get_next(grid, current):
    x, y = current
    pattern = pipes[grid[y][x]]
    adjacents = []
    for x2, y2 in pipes[grid[y][x]]:
        must_accept = [x2, y2]
        if must_accept in pipes[grid[y+y2][x+x2]]:
            adjacents += [[x+x2, y+y2]]
    return adjacents

steps = 0
passed[currents[0][1]][currents[0][0]] = steps
next_currents = []

while len(currents) > 0:
    steps += 1
    for cur in range(len(currents)):
        cur = currents[cur]
        next = get_next(lines, cur)
        next = list(filter(lambda n: passed[n[1]][n[0]] == -1, next))
        for n in next:
            next_currents += [n]
            passed[n[1]][n[0]] = steps
    currents = next_currents
    next_currents = []

debug_print(lines, passed)
total = max([max(l) for l in passed])


file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')