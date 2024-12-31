from operator import sub,truediv
from math import ceil,log
f = open("input","r")
data = f.read().split("\n")
seqs = []
sols = []
for i in data:
    x,y = i.split(": ")
    sols.append(int(x))
    seqs.append(list(map(int,y.split())))

def re_cat(a,b):
    return (a-b) / (10 ** int(log(b,10)+1))
# part 1
def find(sol,seq, ops):
    if len(seq) == 1:
        return sol == seq[0]

    x, *rest = seq
    for op in ops:
        if find(op(sol, x), rest, ops):
            return sol
    return 0

result = 0
result2 = 0
for sol,seq in zip(sols,seqs):
    seq.reverse()

    # part 1
    result += find(sol,seq,[sub,truediv])

    # part 2
    result2 += find(sol,seq,[sub,truediv,re_cat])

print(f"result part 1 : {result}")
print(f"result part 2 : {result2}")