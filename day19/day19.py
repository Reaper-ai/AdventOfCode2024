import itertools

towels, combinations = open("input","r").read().split("\n\n")
towels = towels.split(", ")
combinations = combinations.split("\n")

def can_construct(target, word_bank, part1=False):

    dp = [0] * (len(target) + 1)
    dp[0] = 1

    for i in range(len(target) + 1):
        if dp[i]:
            for word in word_bank:
                if target[i:i+len(word)] == word:
                    if part1: # part 1
                        dp[i+len(word)] = 1
                    else: # part 2
                        dp[i+len(word)] += dp[i]
    return dp[len(target)]

# part 1
result = 0
for towel in combinations:
    result += can_construct(towel, towels,True)
print("result part 1",result)

# part 2
result = 0
for towel in combinations:
    result += can_construct(towel, towels)
print("result part 1",result)
