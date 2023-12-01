input = open("input.txt", "r").read()

lines = input.split('\n')

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def word_to_dig(s):
    if s == 'one':
        return 1
    elif s == 'two':
        return 2
    elif s == 'three':
        return 3
    elif s == 'four':
        return 4
    elif s == 'five':
        return 5
    elif s == 'six':
        return 6
    elif s == 'seven':
        return 7
    elif s == 'eight':
        return 8
    elif s == 'nine':
        return 9
    return int(s)

def find_first(s):
    for w in words:
        if s[0:len(w)] == w:
            return w
    return find_first(s[1:])

def find_last(s):
    for w in words:
        if s[-len(w):] == w:
            return w
    return find_last(s[:-1])

total = 0

for i in lines:
    first = find_first(i)
    last = find_last(i)
    total += (word_to_dig(first)*10) + word_to_dig(last)

print(total)


# total = 0
# for i in lines:
#     min_pos = 10000000
#     for w in words:
#         pos = i.find(w)
#         if pos != -1:
#             if pos < min_pos:
#                 min_pos = pos
    # nums = []
    # for j in i:
    #     if j.isdigit():
    #         nums += j
    # part = int(nums[0] + nums[-1])
    # print(part)
    # total += part
print(total)