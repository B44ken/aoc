import sys, re
if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)
input = open(sys.argv[1], 'r').read()
lines = input.split('\n')

copies = [1 for i in lines]
wins = [0 for i in lines]


total = 0
for i, line in enumerate(lines):
    line = line.split(': ')[1]
    lucky = []
    winning = []
    collect_points = False
    for word in line.split(' '):
        if collect_points and word.strip() in lucky and word != '':
            winning += [word]
        if word == '|':
            collect_points = True
        else:
            lucky += [word]
    points = len(winning)
    wins[i] = points
    for j in range(points):
        copies[j+i+1] += copies[i]


for i in range(len(copies)):
    print(f'{i}: {wins[i]}, {copies[i]}')
    total += copies[i]



file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')