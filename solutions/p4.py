from functools import reduce
from operator import add

with open('inputs/i4.txt', 'r') as file:
    lines = file.read().strip().split('\n')
    m = len(lines)
    n = len(lines[0])
    mat = [[None for _ in range(m)] for _ in range(n)]
    i = 0
    for line in lines:
        j = 0
        for letter in line:
            mat[i][j] = letter
            j += 1
        i += 1

# ----------------------- Part I -------------------------------

def is_useful(word):
    return True if word == "XMAS" or word == "SAMX" else False


def check_horizontal(mat):
    count = 0
    for row in mat:
        for i in range(0,len(row)-3):
            word = "".join(row[i:i+4])
            if is_useful(word):
                count += 1
    return count


def check_vertical(mat,m,n):
    count = 0
    for i in range(m-3):
        for j in range(n):
            word = "".join(mat[i + k][j] for k in range(4))
            if is_useful(word):
                count += 1
    return count


def check_diagonals1(mat,m,n):
    count = 0
    for i in range(m-3):
        for j in range(n-3):
            word = "".join(mat[i + k][j + k] for k in range(4))
            if is_useful(word):
                count += 1
    return count


def check_diagonals2(mat,m,n):
    count = 0
    for i in range(m-3):
        for j in range(3,n):
            word = "".join(mat[i + k][j - (3 - k)] for k in range(4))
            if is_useful(word):
                count += 1
    return count


reduce(add,
       [check_horizontal(mat),
        check_vertical(mat,m,n),
        check_diagonals1(mat,m,n),
        check_diagonals2(mat,m,n)])


# ----------------------- Part II -------------------------------

def is_useful_matrix(sub_matrix):
    word1 = "".join(sub_matrix[k][k] for k in range(3))
    word2 = "".join(sub_matrix[k][2-k] for k in range(2,-1,-1))
    if (word1 == "MAS" or word1 == "SAM") and (word2 == "MAS" or word2 == "SAM"):
        return True
    else:
        return False


def check_sub_matrices(mat,m,n):
    count = 0
    mat_list = list()
    for i in range(m-2):
        for j in range(n-2):
            sub_mat = [row[i : i +3] for row in mat[j : j + 3]]
            if is_useful_matrix(sub_mat):
                count += 1
    return count

print(check_sub_matrices(mat,m,n))
