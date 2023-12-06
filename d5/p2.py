import sys, re, itertools

if len(sys.argv) < 2:
    print('python3 sol.py <input file> <n>')
    print('day 5 is run diffrerently, n is the chunk number [0-9]')
    exit(1)

input = open(sys.argv[1], 'r').read()
lines = input.split('\n\n')

map_chain = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

# slr = [3810626561, 257826205]
slr = [4068426561 - 100_000, 100_000]
seed_list = []
for s in range(slr[0], slr[0] + slr[1], 100_000):
    seed_list += [s, 100_000]
print(slr)
# seed_list = [int(i) for i in re.findall(r'\d+', lines[0])]

# if len(sys.argv) == 3:
#     chunk = int(sys.argv[2])
#     seed_list = seed_list[chunk*2:chunk*2+2]
# upper bound = 2768531151
for s in range(len(seed_list[::2])):
    start = seed_list[2*s]
    seeds = []
    for i in range(seed_list[2*s], seed_list[2*s] + seed_list[2*s+1], 1):
        seeds += [i]
    print('seeds: ', len(seeds), ', start: ', seeds[0])
    for map_i, map in enumerate(lines[1:]):
        map_type = re.findall('\w+-to-\w+', map)[0].split('-to-')
        # print('part: ', map_type[0])
        log_target = 1
        # s_cf = 100.0 / len(seeds)
        for s_i in range(len(seeds)):
            # if s_i == log_target:
            #     log_target *= 3
            #     print('progress: ', s_i * s_cf)
            for line in map.split('\n')[1:]:
                destination, source, length = [int(i) for i in line.split(' ')]
                if seeds[s_i] >= source and seeds[s_i] <= (source + length):
                    seeds[s_i] = destination + (seeds[s_i] - source)
                    break
    print('lowest:', min(seeds))

total = min(seeds)

print('total: ', total)

# file_name = sys.argv[1].replace(".txt", "")
# file_padding = " " * (10 - len(file_name))
# print(f'{file_name}{file_padding}{total}')