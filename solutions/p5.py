from collections import defaultdict
from functools import cmp_to_key

# Part I

## Reading and structuring input
order = defaultdict(set)
arrays = []
with open('inputs/i5.txt', 'r') as file:
    get_seq = False
    for line in file:
        if line.strip() == "":
            # Input structure changes here.
            get_seq = True
        elif get_seq == False:
            num1,num2 = line.split("|")[0],line.split("|")[1].strip()
            order[num1].add(num2)
        elif get_seq:
            arrays.append(line.strip().split(","))

def get_next_elements(num):
    return order[num]

## Validate arrays order
def is_valid_order(sequence):
    for i in range(len(sequence)):
        if not set(sequence[i+1:]) <= get_next_elements(sequence[i]):
            return False
    return True


def get_middle_element(sequence):
    return int(sequence[(len(sequence)-1)//2])


def get_count(arrays):
    count = 0
    for seq in arrays:
        if is_valid_order(seq):
            count += get_middle_element(seq)
    return count


# Part II
def compare(num1, num2):
    if num2 not in get_next_elements(num1):
        return False
    else:
        return True

## Uses bubble sort
def rectify_order(seq):
    n = len(seq)
    for i in range(n):
        for j in range(n - i - 1):
            if compare(seq[j],seq[j+1]):
                seq[j],seq[j+1] = seq[j+1],seq[j]


def get_rectified_count(arrays):
    count = 0
    for seq in arrays:
        if not is_valid_order(seq):
            rectify_order(seq)
            count += get_middle_element(seq)
    return count
