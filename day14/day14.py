import re
import numpy as np
from math import sqrt

robots = [list(map(int, re.findall(r"\d+|-\d+", i))) for i in open("input","r").read().split("\n")]
robots = [[[robo[0],robo[1]],[robo[2], robo[3]]] for robo in robots]
W = 101
H = 103

def move(i,t=100):
    cx, cy = robots[i][0]
    vx, vy = robots[i][1]

    nx, ny = cx + t * vx, cy + t * vy
    nx = nx % W
    ny = ny % H

    return (nx, ny)

# part 1
finalpos = []
for i in range(len(robots)):
    finalpos.append(move(i))

Q1,Q2,Q3,Q4 = 0,0,0,0
for pos in finalpos:
    nx, ny = pos

    if nx == W // 2 or ny == H // 2:
        continue
    if nx < W // 2 and ny < H // 2:
        Q1 += 1
    elif nx > W // 2 and ny < H // 2:
        Q2 += 1
    elif nx < W // 2 and ny > H // 2:
        Q3 += 1
    else:
        Q4 += 1

result = Q1*Q2*Q3*Q4
print(f"result part 1 {result}")

# part 2
entropies = []
K = 10000
for t in range(1,K):
    finalpos = []
    for i in range(len(robots)):
        x, y = move(i,t)
        finalpos.append(sqrt(x**2+y**2))
    std_dev = np.std(finalpos)
    entropies.append(std_dev)

res = entropies.index(min(entropies))+1
print(f"result part 2 {res}")


# print easter egg
finalpos = []
for i in range(len(robots)):
    finalpos.append(move(i,res))
img = [["."]*103 for i in range(101)]
for (i,j) in finalpos:
    img[i][j] = "#"
for p in img:
    print(p)