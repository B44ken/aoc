import re

input = open('input.txt', 'r').read()
lines = input.split('\n')

def get_cubes(input, color):
    most = 0 
    for i in re.findall(r'\d+ ' + color, input):
        most = max(int(i.split(' ')[0]), most)
    return most

MAX_BLUE = 14
MAX_RED = 12
MAX_GREEN = 13

total = 0
for i in lines:
    blue = get_cubes(i, 'blue')
    red = get_cubes(i, 'red')
    green = get_cubes(i, 'green')
    # if blue <= MAX_BLUE and red <= MAX_RED and green <= MAX_GREEN:
    #     id = int(i.split(' ')[1][:-1])
    #     total += id
    total += red * green * blue

print(total)