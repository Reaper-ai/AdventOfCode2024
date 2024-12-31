from collections import defaultdict
from functools import cache

initial_num = list(map(int,open("input").read().split("\n")))
@cache
def generate(secret):
    def mix(a, b): return a ^ b

    def prune(a): return a % 16777216

    s1 = prune(mix(secret,secret*64))
    s2 = prune(mix(s1,s1//32))
    s3 = prune(mix(s2,s2*2048))

    return s3

L = len(initial_num)
result = 0
prices = [[num%10] for num in initial_num]
for i in range(L):
    num = initial_num[i]
    for _ in range(2000):
        num = generate(num)

    result+=num

print("result part 1:",result)

# part 2
total_bananas = defaultdict(int)
for num in initial_num:
    seen = set()
    diffs = []
    for i in range(2000):
        next_num = generate(num)
        diffs.append((next_num % 10) - (num % 10))
        num = next_num
        if i >= 3:
            sequence = tuple(diffs)
            if sequence not in seen:
                total_bananas[sequence] += num % 10
                seen.add(sequence)
            diffs.pop(0)

print("result part 2 ",max(total_bananas.values()))