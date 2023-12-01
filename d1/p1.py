input = open("input.txt", "r").read()
lines = input.split('\n')

total = 0
for i in lines:
    nums = []
    for j in i:
        if j.isdigit():
            nums += j
        part = int(nums[0] + nums[-1])
        total += part

print(total)