from collections import deque
bytes = [tuple(map(int, reversed(line.strip().split(',')))) for line in open('input').readlines()]

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def bfs(bytes):
    #bytes = set(bytes)
    queue = deque([(0, 0, 0)])
    end = (70, 70)
    seen = {(0, 0)}
    while queue:
        x, y, steps = queue.popleft()
        if (x,y) == end:
            return steps

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 71 and 0 <= ny < 71 and (nx,ny) not in bytes:
                if (nx, ny) not in seen:
                    seen.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
    return None

KB = bytes[:1024]
print("result part 1",bfs(KB))

l = 1024
r = len(bytes)
while l < r:
    mid = (l+r)//2
    B = bytes[:mid]
    if bfs(B) is None:
        r = mid
    else:
        l = mid +1

print("result part 2",bytes[l-1][::-1])
