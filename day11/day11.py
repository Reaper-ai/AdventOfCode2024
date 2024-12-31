from collections import defaultdict

stones = list(map(int, open("input","r").read().strip().split()))

#part 1
def part1(st, n):
    for i in range(n):
        for i in range(len(st)):
            if st[i] == 0:
                st[i] = 1
            elif len(str(st[i]))%2 == 0:
                sti = str(st[i])
                st.append(int(sti[len(sti)//2:]))
                st[i] = int(sti[:len(sti)//2])
            else:
                st[i] *= 2024

    return len(st)

print(f"result part 1 {part1(stones[:],25)}")


# part 2
sto = defaultdict(int,)
for i in stones:
    sto[i] = 1

def part2(st, n):

    for i in range(n):
        copy = dict(st)
        for key,value in copy.items():
            if value == 0: continue
            if key == 0:
                st[1] += value
                st[0] -= value
            elif len(str(key))%2 == 0:
                sti = str(key)
                st[int(sti[len(sti)//2:])] += value
                st[int(sti[:len(sti)//2])] += value
                st[int(sti)] -= value
            else:
                st[key*2024] += value
                st[key] -=value
    return sum(st.values())

print(f"result part 2 {part2(sto,75)}")

