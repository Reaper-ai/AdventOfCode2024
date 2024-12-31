import heapq
from collections import defaultdict
import math

maze = [list(i) for i in open("input","r").read().split("\n")]
L = len(maze)
M = len(maze[0])
directions = {(-1,0),(0,-1),(0,1),(1,0)}

walls = set()
# find start end and walls
for i in range(L):
    for j in range(M):
        if maze[i][j] == "S":
            start = (i,j,0,1)

        if maze[i][j] == "E":
            end = (i,j)

        if maze[i][j] == "#":
            walls.add((i,j))

ends = [end+direction for direction in directions]

def neighbours(state):
    r, c, dr, dc = state
    neighbour = []
    if (r+dr,c+dc) not in walls:
        neighbour.append([(r+dr,c+dc,dr,dc),1])
    for ndr,ndc in directions:
        if (ndr,ndc) != (dr,dc):
            neighbour.append([(r,c,ndr,ndc),1000])
    return neighbour
def dijkstra():
    visited = {}
    frontier = [(0, start)]
    cost_dict = defaultdict(lambda: float("inf"), {start:0})
    while frontier:
        cur_cost, cur_pos = heapq.heappop(frontier)

        if cur_pos in visited:
            continue

        visited[cur_cost] = 1
        if cur_pos in ends:
            return cur_cost

        for new_pos,move_cost in neighbours(cur_pos):
            if new_pos not in visited:
                if cur_cost+move_cost < cost_dict[new_pos]:
                    cost_dict[new_pos] = cur_cost+move_cost
                    heapq.heappush(frontier,(cur_cost+move_cost,new_pos))

    return float("inf")

result = dijkstra()
print(f"result part 1: {result}")



def part2(starts):
    visited = {}
    frontier = [(0,start) for start in starts]
    cost_dict = defaultdict(lambda: float("inf"), {start:0 for start in starts})
    path = dict()
    while frontier:
        cur_cost,cur_pos = heapq.heappop(frontier)
        if cur_pos in visited:
            continue
        else:
            path[cur_pos] = cur_cost

        visited[cur_pos] = 1
        for new_pos,move in neighbours(cur_pos):
            new_cost = cur_cost+move
            if new_pos not in visited:
                if new_cost < cost_dict[new_pos]:
                    cost_dict[new_pos] = new_cost
                    heapq.heappush(frontier,(new_cost,new_pos))

    return path


dstart = part2([start])
dend = part2(ends)

seats = set()
for (r,c,dr,dc) in dstart:
    if dstart[(r,c,dr,dc)]+dend[(r,c,-dr,-dc)] == result:
        seats.add((r,c))

print(f"result part 2: {len(seats)}")
