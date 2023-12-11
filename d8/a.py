import sys, re, math

if len(sys.argv) < 2:
    print('python3 sol.py <input file>')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n')

ins = lines[0]
loc = []

m = {}

for l in lines[2:]:
    w = [i for i in re.findall(r"[0-9A-Z]+", l)]
    m[w[0]] = [w[1], w[2]]
    if w[0][2] == 'A':
        loc.append(w[0])

print(loc, ins, m)


total = 1
for l in loc:
    r = 0
    while l[2] != 'Z':
        for i in ins:
            if i == 'R':
                l = m[l][1]
            else:
                l = m[l][0]
            r += 1
    print(r)

    total = math.lcm(total, r)

file_name = sys.argv[1].replace(".txt", "")
file_padding = " " * (20 - len(file_name))
print(f'{file_name}{file_padding}{total}')
