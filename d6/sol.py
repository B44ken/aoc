import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')

def ways_to_win(dist, time):
    ways = 0
    for i in range(1, time - 1):
        if i * (time - i) > dist:
            ways += 1
    return ways

total = 1

times, distances = [ [int(i) for i in l.split()[1:]] for l in lines ]
for i in range(len(times)):
    total *= ways_to_win(distances[i], times[i])

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')