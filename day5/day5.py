from functools import cmp_to_key
f = open("input", "r")
data = f.read()
order, manuals = data.split("\n\n")
order = [tuple(i.split("|")) for i in order.split("\n")]
manuals = [i.split(",") for i in manuals.split("\n")]
result, result2 = 0,0

# for part 2
def sortfx(a,b):
    if (a,b) in order: return -1
    elif (b,a) in order: return 1
    else: return 0

for man in manuals:
    updates ={ man[i]:i for i in range(len(man))}
    right = True
    for x,y in order:
        if x in updates and y in updates:
            if updates[x] > updates[y]:
                right = False
                break

    # for part 1
    if right:
        result += int(man[len(man)//2])

    # for part 2
    if not right:
        man = sorted(man, key=cmp_to_key(sortfx))
        result2 += int(man[len(man)//2])



print(f"result part 1 : {result}")
print(f"result part 2 : {result2}")
