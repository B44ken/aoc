import sys, re

if len(sys.argv) < 2:
	print('python3 sol.py <input file>')
	exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

def transpose(grid):
	return [''.join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]

def rotate(grid):
	return [''.join([grid[j][i] for j in range(len(grid) - 1, -1, -1)]) for i in range(len(grid[0]))]

def rotate_ccw(grid):
	return [''.join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]) - 1, -1, -1)]

spacer = '-' * 12 + '\n'

for i in range(4):
	shift = []
	for L in transpose(lines):
		while L.find('.O') != -1:
			L = L.replace('.O', 'O.')
		shift += [L]
	lines = rotate_ccw(transpose(shift))

print('\n'.join(rotate(shift)))

exit(0)

for i, s in enumerate(shifted):
	total += s.count('O') * (len(shifted) - i)

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')	