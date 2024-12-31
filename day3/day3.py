import re

f = open("input","r")
data = f.read()


def mul(a, b): return a * b

# part 1
result = 0
pattern = r'mul\(\b\d{1,3}\b,\b\d{1,3}\b\)'
muls = re.findall(pattern,data)
for i in muls:
    result += eval(i)

print(f"result part 1 : {result}")

# part 2
result = 0
pattern = r'(mul\(\b\d{1,3}\b,\b\d{1,3}\b\)|do\(\)|don\'t\(\))'
ops = re.findall(pattern,data)
flag = True
print(ops)
for i in ops:
    if i == "do()":
        flag = True
    elif i == "don't()":
        flag = False
    else:
        if flag:
            result += eval(i)

print(f"result part 2 : {result}")

