from collections import defaultdict
f = open("input","r")
map = f.read().split("\n")

X = len(map)
Y = len(map[0])

antenas = defaultdict(list)
for i in range(X):
    for j in range(Y):
        if map[i][j] != ".":
            antenas[map[i][j]].append((i,j))

antinodes = set()
# part 1
for ant in antenas:
    coords = antenas[ant]
    for i in range(len(coords)):
        for j in range(i):
            x1,y1 = coords[i]
            x2, y2 = coords[j]

            ax2, ay2 = 2*x2-x1, 2*y2-y1
            ax1, ay1 = 2*x1-x2, 2*y1-y2


            if ax1 in range(X) and ay1 in range(Y):
                antinodes.add((ax1,ay1))
            if ax2 in range(X) and ay2 in range(Y):
                antinodes.add((ax2,ay2))

print(f"result part 1 : {len(antinodes)}")

# part 2
antinodes = set()
result = 0
for ant in antenas:
    coords = antenas[ant]
    for i in range(len(coords)):
        for j in range(i):
            x1,y1 = coords[i]
            x2, y2 = coords[j]

            mx, my = x2-x1, y2-y1
            ax2, ay2 = x2, y2
            ax1, ay1 = x1, y1
            while ax1 in range(X) and ay1 in range(Y):
                antinodes.add((ax1,ay1))
                ax1 -= mx
                ay1 -= my


            while ax2 in range(X) and ay2 in range(Y):
                antinodes.add((ax2,ay2))
                ax2 += mx
                ay2 += my


result = len(antinodes)
print(f"result part 2 : {result}")