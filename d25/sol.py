import sys, re, igraph

if len(sys.argv) < 2:
	print('python3 sol.py <input file>')
	exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')
total = 0

hail = []

for l in lines:
	px, py, pz, vx, vy, vz = [int(i) for i in re.findall(r'-?\d+', l)]
	hail += [px, py, pz, vx, vy, vz]
    
for A in hail:
	for B in hail:
		if A == B:
			continue
		x = A[0] - B[0]
		y = A[1] - B[1]
		
		
    
file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')