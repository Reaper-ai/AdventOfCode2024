import heapq
from collections import defaultdict,deque

maze = [list(i) for i in open("input").read().split("\n")]
L = len(maze)
M = len(maze[0])

walls = set()
graph = set()
for x in range(L):
    for y in range(M):
        if maze[x][y] == ".":
            graph.add(complex(x,y))

        if maze[x][y] == "S":
            start = complex(x,y)
            graph.add(start)
        if maze[x][y] == "E":
            end = complex(x,y)
            graph.add(end)

        if maze[x][y] == "#":
            walls.add(complex(x,y))

directions = [1, -1, 1j, -1j]
def flood_fill(maze, start):
    distances = defaultdict(lambda :float("inf"))
    distances[start] = 0

    queue = deque([start])

    while queue:
        current = queue.popleft()

        for direction in directions:
            neighbor = current + direction

            if neighbor in maze and distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances


all_distances = dict(flood_fill(graph,end))

# part 1
cheats = defaultdict(int)
def dijkstra(maze, start, end):

    distances = defaultdict(lambda : float('inf'))
    distances[start] = 0

    parents = {start: None}


    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_point = heapq.heappop(priority_queue)

        if current_point == end:
            break

        for direction in directions:
            neighbor = current_point + direction

            if neighbor in maze:
                distance = current_distance + 1
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    parents[neighbor] = current_point
                    heapq.heappush(priority_queue, (distance, neighbor))

            if neighbor in walls:
                if neighbor + direction in all_distances:
                    cut = all_distances[current_point] - all_distances[neighbor+direction]
                    if cut-2 >= 100:
                        cheats[cut-2] +=1



dijkstra(graph, start, end)
print("result part 1", sum(cheats.values()))


# part 2
cheats = defaultdict(int)
for key1 in all_distances:
    for key2 in all_distances:
        if abs(key2.real - key1.real) + abs(key2.imag - key1.imag) <= 20:
            dist = all_distances[key1] - all_distances[key2] - (abs(key2.real - key1.real) + abs(key2.imag - key1.imag))
            if dist >= 100:
                cheats[dist] +=1


print("result part2 ", sum(cheats.values()))