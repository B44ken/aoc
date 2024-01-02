import sys, re

if len(sys.argv) < 2:
	print('python3 sol.py <input file>')
	exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split(',')
total = 0

# def transpose(grid):
# 	return [''.join([grid[j][i] for j in range(len(grid))]) for i in range(len(grid[0]))]

def rotate(grid):
	return [''.join([grid[j][i] for j in range(len(grid))][::-1]) for i in range(len(grid[0]))]

def hash(st):
	cur = 0
	for c in st:
		cur += ord(c)
		cur *= 17
		cur = cur % 256
	return cur

for line in lines:
	total += hash(line)


file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')	