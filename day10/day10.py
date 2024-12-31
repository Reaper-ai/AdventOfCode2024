
map = [list(map(int,list(i))) for i in open("input","r").read().split("\n")]

L = len(map)
M = len(map[0])
starts = []

for i in range(L):
    for j in range(M):
        if map[i][j] == 0:
            starts.append((i,j))

def dfs(grid,x,y,visited, for_part1 = True):
    stack = [(x, y)]
    found_nines = list()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while stack:
        cx, cy = stack.pop()

        if for_part1:
            if (cx, cy) in visited:
                continue

            visited.add((cx, cy))

        if grid[cx][cy] == 9:
            found_nines.append((cx, cy))
            continue

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < L and 0 <= ny < M and grid[nx][ny] == grid[cx][cy] + 1:
                stack.append((nx, ny))
    return len(found_nines)

#part 1
result = 0
for i, j in starts:
    result += dfs(map, i, j, set())

print(f"result part 1 {result}")
result = 0
for i, j in starts:
    result += dfs(map, i, j, set(), False)
print(f"result part 2 {result}")