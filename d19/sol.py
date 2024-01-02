import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

flows_str, parts_str = [part.split('\n') for part in input.split('\n\n')]
flows, parts = {}, []

for part in parts_str:
    part = part[1:-1].split(',')
    vals = {}
    for p in part:
        k, v = p.split('=')
        vals[k] = v
    parts += [vals]

for flow in flows_str:
    flow = flow[:-1]
    name, steps = flow.split('{')
    steps = steps.split(',')
    flows[name] = steps

for part in parts:
    current = flows['in']
    status = None
    step_n = 0
    while status == None:
        step = current[step_n]
        step_n += 1

        good = False

        colon = step.split(':')
        if len(colon) == 1:
            pass
        elif '<' in colon[0]:
            key, value = colon[0].split('<')
            if int(part[key]) >= int(value):
                continue
        elif '>' in colon[0]:
            key, value = colon[0].split('>')
            if int(part[key]) <= int(value):
                continue

        if colon[-1] == 'A':
            status = 'A'
        elif colon[-1] == 'R':
            status = 'R'
        else:
            current = flows[colon[-1]]
            step_n = 0
    print(status)
    if status == 'A':
        total += sum([int(i) for i in part.values()])

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')