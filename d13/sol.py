import sys, re

if len(sys.argv) < 2:
	print('python3 sol.py <input file>')
	exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

def transpose(grid):
	return [''.join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]

grids = [i.split('\n') for i in input.split('\n\n')]

def is_mirror(a, b, grid, prev_diffs=0):
	if a < 0 or b == len(grid):
		return prev_diffs == 1
	diffs = 0
	for i in range(len(grid[a])):
		if grid[a][i] != grid[b][i]:
			diffs += 1
	return is_mirror(a - 1, b + 1, grid, prev_diffs + diffs)
	
for grid in grids:
	grid = transpose(grid)
	has_column = False
	for line in range(1, len(grid)):
		if is_mirror(line-1, line, grid):
			print(grid[line], line)
			total += line
	grid = transpose(grid)
	if has_column:
		continue
	for line in range(1, len(grid)):
		if is_mirror(line-1, line, grid):
			print(grid[line], line)
			total += line * 100


file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')