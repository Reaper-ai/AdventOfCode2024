f = open("input", "r")
data = f.read().split("\n")
l1, l2 = [],[]
for i in data:
    x,y = i.split("   ")
    l1.append(int(x))
    l2.append(int(y))

# part1
l1.sort()
l2.sort()
dist = 0
for i,j in zip(l1,l2):
    dist += abs(i - j)

print(f"result part 1 {dist}")

# part 2
d = dict()
for i in l1:
    if i not in d:
        d[i] = (l1.count(i), l2.count(i))

s_score = 0
for key in d:
    s_score += (key * d[key][0] * d[key][1])

print(f"result part 2 {s_score}")