import sys, re

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n\n')

seeds = [int(i) for i in re.findall(r'\d+', lines[0])]

# for map in lines:
#     print(map)

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (10 - len(file_name))
print(f'{file_name}{file_padding}{total}')