import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')

total = 0
for i in lines:
    pass

print(total)

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * 20 - len(file_name)
print(f'{file_name}{file_padding}{total}')