
rhs = []
lhs = []
with open("inputs/i7.txt", 'r') as file:
    for line in file:
        [r,l] = line.strip().split(":")
        rhs.append(int(r))
        lhs.append(list(map(int, l.strip().split(' '))))


def process_nums(target, curr, nums, n):
    if curr == target:
        return True
    elif n == len(nums):
        return False
    else:
        return process_nums(target, curr + nums[n], nums, n+1) or \
               process_nums(target, curr * nums[n], nums, n+1) or \
               process_nums(target, int(str(curr) + str(nums[n])), nums, n+1)

def process_all(rhs, lhs):
    input_len = len(rhs)
    i = 0
    count = 0
    while i < input_len:
        if process_nums(rhs[i], lhs[i][0], lhs[i], 1):
            count += rhs[i]
        i += 1
    return count


process_all(rhs,lhs)
