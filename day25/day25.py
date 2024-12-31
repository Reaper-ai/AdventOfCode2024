import numpy as np
schematics = [[list(j)for j in i.split("\n")] for i in open("input").read().split("\n\n")]


def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed


for i in range(len(schematics)):
    schematics[i] = transpose(schematics[i])

locks = []
keys = []
for sch in schematics:
    temp = []
    for row in sch:
        temp.append(row.count("#"))

    if sch[0][0] == "#":
        locks.append(np.array(temp)-1)
    else:
        keys.append(np.array(temp)-1)

result = 0

for lock in locks:
    for key in keys:
        fit = lock+key
        if all(fit < 6):
            result +=1


print(result)