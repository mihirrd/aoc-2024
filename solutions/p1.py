import os
from collections import defaultdict

# Part I
def sum_distances(l1, l2):
    arr = [[0]*len(l1),[0]*len(l2)]
    arr[0] = sorted(l1)
    arr[1] = sorted(l2)
    result = 0
    for i in range(0,len(l1)):
        result += abs(arr[0][i] - arr[1][i])
    return result


# Part II
def similarity_score(l1,l2):
    l2_freq = defaultdict(int)
    result = 0
    for i in l2:
        l2_freq[i] += 1
    for i in l1:
        result += i * l2_freq[i]
    return result        


def read_input(f):
    l1 = []
    l2 = []
    with open(f,'r') as file:
        for line in file:
            line = line.strip().split()
            l1.append(int(line[0]))
            l2.append(int(line[1]))
    return l1,l2


l1,l2 = read_input('inputs/i1.txt')

# sum_distances(l1,l2)
# similarity_score(l1,l2)
