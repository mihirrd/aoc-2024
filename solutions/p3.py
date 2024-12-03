import re

def process_op(op):
    nums = [int(i) for i in re.findall(r"mul\((\d+),(\d+)\)", op)[0]]
    return nums[0]*nums[1]


with open('inputs/i3.txt', 'r') as file:
    result = 0
    line = file.read().strip()
    m = re.findall(r"mul\(\d+,\d+\)|don't|do", line)
    process = True
    for op in m:
        if op == "don't":
            process = False
            continue
        if op == "do":
            process = True
            continue
        if process:
            result += process_op(op)

    print(result)
