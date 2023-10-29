def bfs(grid, i,  j):
    import collections
    if not grid:
        return []
    q = collections.deque()
    q.append([i,j])

    while q:
        r,c = q.popleft()
        for nr,nc in [(r+1,c), (r,c+1),(r,c-1),(c,r-1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                grid[nr][nc] = 2
                q.append([nr,nc])
    return (r,c)


def copy_matrix(x):
    from copy import deepcopy
    y = deepcopy(x)
    return y




#1
def find_co(grid):
    ls = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                r = bfs(grid, i, j)
                ls.append([(i,j), r])
    return ls

#2
#1
def find_co2(grid):
    m =copy_matrix(grid)
    ls = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                r = bfs(m, i, j)
                ls.append([(i,j), r])
    return ls

def find_co3(grid):
    m =copy_matrix(grid)
    ls = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == 0:
                r = bfs(m, i, j)
                ls.append([(i,j), r])
    return ls


