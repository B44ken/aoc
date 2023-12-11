import sys, re
from math import lcm

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')

graph = {}
instructions = list(lines[0])

for line in lines[2:]:
    rxp = re.match('(.{3}) = \((.{3}), (.{3})\)', line)
    node = rxp.group(1)
    graph[node] = { 
        'L': rxp.group(2),
        'R': rxp.group(3)
    }

starts = [i for i in graph.keys() if i[2] == 'A']
steps = []

for s in starts:
    current = s
    step = 0
    while current[2] != 'Z':
        for ins in instructions:
            current = graph[current][ins]
            step += 1
    steps += [step]

print(lcm(*steps))