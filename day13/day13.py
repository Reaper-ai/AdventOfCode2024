import re
import numpy as np
from collections import defaultdict


mechines = [i.split("\n") for i in open("input","r").read().split("\n\n")]

systems = []

for mechine in mechines:
    mech = defaultdict(list)
    a = list(map(int,re.findall(r"\d+",mechine[0])))
    b = list(map(int,re.findall(r"\d+",mechine[1])))
    mech["X"] = [a[0], b[0]]
    mech["Y"] = [a[1], b[1]]
    mech["prize"] = list(map(int,re.findall(r"\d+",mechine[2])))
    systems.append(mech)


def solve(mul=0):
    solutions = []
    for eqs in systems:
        try:
            S = np.linalg.solve(np.array([eqs["X"],eqs["Y"]]),np.array(eqs["prize"])+mul)
            if np.all(np.abs(S - np.round(S)) < 1E-4): # floating point go brrr
                 solutions.append(S)
        except np.linalg.LinAlgError:
            continue

    return solutions

result = 0
# part 1
solutions = solve()
for s in solutions:
    result += (3*s[0] + s[1])

print(f"result part 1 : {result}")

# part 2
result = 0
solutions = solve(10000000000000)
for s in solutions:
    result += (3*s[0] + s[1])

print(f"result part 2 : {result}")

