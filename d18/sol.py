import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

dirs = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1)
}

x, y = 0, 0
min_x, min_y = 0, 0
max_x, max_y = 0, 0

for l in lines:
    _, _, hex = l.split()
    n = int(hex[2:5], 16)
    dir = ('RDLU')[int(hex[-2], 16)]
    dx, dy = dirs[dir]
    x += dx * n
    y += dy * n
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

print(min_x, min_y, max_x, max_y)

grid = [['.' for x in range(max_x - min_x + 1)] for y in range(max_y - min_y + 1)]
x, y = -min_x, -min_y

I = 0
for l in lines:
    _, _, hex = l.split()
    n = int(hex[2:5], 16)
    dir = ('RDLU')[int(hex[-2], 16)]
    dx, dy = dirs[dir]
    for i in range(n):
        grid[y][x] = '#'
        x += dx
        y += dy


ffqueue = [(50, 28)]
while len(ffqueue) > 0:
    x, y = ffqueue.pop()
    if grid[y][x] != '.':
        continue
    # grid[y][x] = '#'
    total += 1
    ffqueue.append((x-1, y))
    ffqueue.append((x+1, y))
    ffqueue.append((x, y-1))
    ffqueue.append((x, y+1))


total = ''.join([''.join(g) for g in grid]).count('#')

# print('\n'.join([''.join(g) for g in grid]))

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')