import copy
from collections import deque

mp, movements = open("input","r").read().split("\n\n")

mp = [list(i) for i in mp.split("\n")]
movements = "".join(movements.split("\n"))
dirs = {"v": (1, 0), ">": (0, 1), "<": (0, -1), "^": (-1, 0)}

H = len(mp)
W = len(mp[0])

def st(l,m, map):
    for i in range(l):
        for j in range(m):
            if map[i][j] == "@":
                start =  (i, j)
                return start

def part_1(map):


    def adjust(x,y,dx,dy):
        cx, cy = x, y
        while map[cx+dx][cy+dy] == "O":
            cx += dx
            cy += dy
        if map[cx+dx][cy+dy] == "#":
            return x,y
        else:
            while (cx,cy) != (x, y):
                map[cx][cy], map[cx+dx][cy+dy] = map[cx+dx][cy+dy], map[cx][cy]
                cx -= dx
                cy -=dy

            return cx+dx,cy+dy

    E = len(movements)
    i = 0
    x, y = st(H,W, map)
    while i != E:
        map[x][y] = "."
        move = movements[i]
        dx, dy = dirs[move]

        if map[x+dx][y+dy] == ".":
            x, y = x+dx, y+dy
        elif map[x+dx][y+dy] == "#":
            x,y = x,y
        elif map[x+dx][y+dy] == "O":
            x,y = adjust(x,y,dx,dy)

        map[x][y] = "@"
        """for k in map:
            print(k)
        print()
        """
        i += 1

    result = 0
    for i in range(H):
        for j in range(W):
            if map[i][j] == "O":
              result += (i*100 +j)


    return result

map = copy.deepcopy(mp)
print(f"result part 1 {part_1(map)}")

# part 2
extended = [[] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if mp[i][j] in ["#","."]:
            extended[i].extend([mp[i][j]]*2)
        elif mp[i][j] == "@":
            extended[i].extend(["@", '.'])
        else:
            extended[i].extend(["[","]"])

dirs = {"v": 1, ">": 1j, "<": -1j, "^": -1}

def bfs(new_pos, boxes, offset):
    visited = set()
    queue = deque([new_pos])
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        queue.append(boxes[current])
        if current + offset in boxes:
            queue.append(current + offset)
    return visited


def part_2(walls, boxes, start):
    pos = start
    for mv in movements:
        dxy = dirs[mv]
        new_pos = pos + dxy
        if new_pos in walls:
            continue
        if new_pos not in boxes:
            pos = new_pos
        else:
            cluster = bfs(new_pos, boxes, dxy)
            cluster_dict = {key + dxy: value + dxy for key, value in boxes.items() if key in cluster}
            if not cluster_dict.keys() & walls:
                boxes = {key: value for key, value in boxes.items() if key not in cluster} | cluster_dict
                pos = new_pos



    return sum(50 * box.real + box.imag / 2 - 0.25 for box in boxes)

def args():
    walls = set()
    boxes = {}
    for i in range(len(extended)):
        for j in range(len(extended[0])):
            if extended[i][j] == "#":
                walls.add(complex(i,j))
            elif extended[i][j] == "[":
                boxes[complex(i, j)] = complex(i, j + 1)
                boxes[complex(i, j + 1)] = complex(i, j)

            if extended[i][j] == "@":
                start = complex(i,j)
    return walls, boxes, start

print(f"result part 2 {part_2(*args())}")
