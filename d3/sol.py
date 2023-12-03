import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')

total = 0
lines = ['.' * len(lines[0])] + lines + ['.' * len(lines[0])]
for i in range(len(lines)):
    lines[i] = '.' + lines[i] + '...'


gears_touching = {}

for i in range(len(lines)):
    dig = 0
    prev_dig = 0
    part = []
    surround = []
    for j in range(len(lines[i])):
        if lines[i][j].isdigit():
            dig = dig * 10 + int(lines[i][j])
            surround = surround + [[i-1, j-1], [i, j-1], [i+1, j-1], [i-1, j], [i+1, j], [i-1, j+1], [i, j+1], [i+1, j+1]]
        else:
            index = ''
            for s in surround:
                if lines[s[0]][s[1]] == '*':
                    part = s
                    index = str(s[0]) + ',' + str(s[1])
            if index:
                if index not in gears_touching:
                    gears_touching[index] = []
                gears_touching[index] += [dig]
            surround = []
            part = []
            dig = 0

for key in gears_touching:
    if len(gears_touching[key]) == 2:
        total += gears_touching[key][0] * gears_touching[key][1]

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')