garden = [list(i) for i in open("input","r").read().split("\n")]

def flood_fill(grid):
    if not grid:
        return []

    def get_neighbors(r, c):
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and (nr, nc) not in visited:
                yield nr, nc

    def bfs(start_r, start_c):
        queue = [(start_r, start_c)]
        visited.add((start_r, start_c))
        region = {(start_r, start_c)}
        while queue:
            r, c = queue.pop(0)
            for nr, nc in get_neighbors(r, c):
                if grid[nr][nc] == grid[r][c] and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    region.add((nr, nc))
                    queue.append((nr, nc))
        return region

    visited = set()
    regions = []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited:
                regions.append(bfs(r, c))

    return regions
# part 1
result = 0
regions = flood_fill(garden)
for region in regions:
    area = len(region)
    if area == 1:
        result += 4
    else:
        rough_pm = 4*area

        region = list(region)
        for i in range(len(region)):
            for j in range(i,len(region)):
                x1,y1 = region[i]
                x2, y2 = region[j]
                if (abs(x1-x2)==1 and abs(y2-y1) == 0) or (abs(x1-x2)==0 and abs(y2-y1) == 1):
                    rough_pm -= 2

        result += (area*rough_pm)

print(f"part 1 result {result}")

# part 2
costs = []
for region in regions:
    corner = 0
    for x,y in region:


        if (x-1, y) in region and (x,y-1) in region and (x-1,y-1) not in region:
            corner += 1
        elif not ((x-1, y) in region or (x,y-1) in region ):
            corner += 1
        if (x-1,y) in region and (x,y+1) in region and (x-1,y+1) not in region:
            corner += 1
        elif not ((x-1,y) in region or (x,y+1) in region ):
            corner += 1
        if (x+1,y) in region and (x,y+1) in region and (x+1,y+1) not in region:
            corner += 1
        elif not ((x+1,y) in region or (x,y+1) in region ):
            corner += 1
        if (x+1,y) in region and (x,y-1) in region and (x+1,y-1) not in region:
            corner += 1
        elif not ((x+1,y) in region or (x,y-1) in region ):
            corner += 1

    costs.append(len(region)*corner)

print(f"result part 2 {sum(costs)}")