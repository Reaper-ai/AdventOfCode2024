f = open("input","r")
map = [list(i) for i in f.read().split("\n")]
X = len(map)
Y = len(map[0])

# find starting position
for i in range(X):
    if "^" in map[i]:
        start = (i, map[i].index("^"))

dx, dy = -1, 0
cx, cy = start
seen = set()
obs = set()
# part 1
def change_dirs(dx, dy):
    if dx == -1 and dy == 0: return (0, 1)
    elif dx == 0 and dy == 1: return (1, 0)
    elif dx == 0 and dy == -1: return (-1, 0)
    elif dx == 1 and dy == 0: return (0, -1)

while cx+dx in range(X) and cy+dy in range(Y):
    if map[cx+dx][cy+dy] != "#":
        seen.add((cx, cy))
        cx, cy = cx + dx,  cy + dy
    else:
        dx, dy = change_dirs(dx, dy)

seen.add((cx,cy))
print(f"result part 1 : {len(seen)}")


candidate = seen - {start}
# part 2
result = 0
for i in seen:
    x,y = i
    map[x][y] = "#"
    flag = False
    posvec = set()
    visited = set()
    dx, dy = -1, 0
    cx, cy = start
    while cx + dx in range(X) and cy + dy in range(Y):
        if map[cx + dx][cy + dy] != "#":
            visited.add((cx, cy))
            if (cx,cy,dx,dy) in posvec:
                flag = True
                break
            posvec.add((cx,cy,dx,dy))
            cx, cy = cx + dx, cy + dy
        else:
            dx, dy = change_dirs(dx, dy)

    result += flag
    map[x][y] = "."


print(f"result part 2 : {result}")



