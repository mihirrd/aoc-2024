class Guard:
    def __init__(self, direction, position):
        self.direction = direction
        self.position = position


    def get_position(self):
        return self.position

    def rotate(self):
        if self.direction == 'u':
            self.direction = 'r'
        elif self.direction == 'r':
            self.direction = 'd'
        elif self.direction == 'd':
            self.direction = 'l'
        elif self.direction == 'l':
            self.direction = 'u'

    def move(self,i,j):
        if self.direction == 'u':
            self.position = [i-1,j]
        if self.direction == 'r':
            self.position = [i,j+1]
        if self.direction == 'd':
            self.position = [i+1,j]
        if self.direction == 'l':
            self.position = [i,j-1]

    def look(self,mat):
        [i,j] = self.position
        if self.direction == 'u' and i > 0:
            return mat[i-1][j]
        if self.direction == 'r' and j < len(mat[i])-1:
            return mat[i][j+1]
        if self.direction == 'd' and i < len(mat)-1:
            return mat[i+1][j]
        if self.direction == 'l' and j > 0:
            return mat[i][j-1]
        return None

# Read and structure input into a 2D matrix
matrix = []
with open("inputs/i6.txt", 'r') as file:
    for line in file:
        row = list(line.strip())
        matrix.append(row)

# Locate the starting position of the guard
def locate_guard(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == '<':
                return Guard('l',[i,j])
            if mat[i][j] == 'v':
                return Guard('d',[i,j])
            if mat[i][j] == '>':
                return Guard('r',[i,j])
            if mat[i][j] == '^':
                return Guard('u',[i,j])


def can_move(guard,mat):
    [x,y] = guard.get_position()
    if guard.look(mat) == '#':
        guard.rotate()
    if guard.look(mat) == None:
        # Last position of the guard.
        mat[x][y] = 'X'
        return False
    return True


def travel(mat):
    guard = locate_guard(mat)
    while can_move(guard,mat):
        [x,y] = guard.get_position()
        mat[x][y] = 'X'
        guard.move(x,y)
    return 0


def trace_path(mat):
    travel(matrix)
    count = 0
    for row in mat:
        for i in row:
            if i == 'X':
                count += 1
    return count

trace_path(matrix)
