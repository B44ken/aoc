import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

def differences(line):
    return [line[i] - line[i-1] for i in range(1, len(line))]

for l in lines:
    l = [int(l) for l in l.split()]
    l.reverse()
    diffs = [l[-1]]
    while sum(l) != 0:
        l = differences(l)
        diffs += [l[-1]]
    print(sum(diffs))
    total += sum(diffs)

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')