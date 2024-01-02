import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
grid = [list(line) for line in input.split('\n')]
total = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            grid[y][x] = True
        if grid[y][x] == '#':
            grid[y][x] = None
        if grid[y][x] == '.':
            grid[y][x] = False

for i in range(64):
    grid_copy = [[False for x in range(len(grid[y]))] for y in range(len(grid))]
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == None:
                grid_copy[y][x] = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            adjacent = [ [y-1, x], [y+1, x], [y, x-1], [y, x+1] ]
            for a in adjacent:
                if a[0] < 0 or a[0] >= len(grid) or a[1] < 0 or a[1] >= len(grid[y]):
                    continue
                if grid[a[0]][a[1]] == True and grid[y][x] == False:
                    grid_copy[y][x] = True
    grid = grid_copy

def replace(cell):
    if cell == True:
        return '#'
    return ' '

# total
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == True:
            total += 1

print('\n'.join([' '.join([replace(cell) for cell in row]) for row in grid]))




file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')