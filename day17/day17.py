import re
import math

regi, program = open("input","r").read().split("\n\n")
A,B,C = [int(re.findall(r"\d+",r)[0]) for r in regi.split("\n")]
program = list(map(int,re.findall(r"\d+",program)))

flow = []

#part 1
def solve(A,B=0,C=0):
    def combo(operand):
        if program[operand] <= 3:
            return program[operand]
        elif program[operand] == 4:
            return A
        elif program[operand] == 5:
            return B
        elif program[operand] == 6:
            return C
    ptr = 0
    output = []
    while ptr < len(program):

        match program[ptr]:
            case 0: #adv
                A = A >> combo(ptr+1)
                flow.append("adv")
            case 1: #bxl
                B = B ^ program[ptr+1]
                flow.append("bxl")
            case 2: #bst
                B = combo(ptr+1)%8
                flow.append("bst")
            case 3: #jnz
                if A !=0:
                    ptr = program[ptr+1]
                    flow.append("jnz")
                    continue
            case 4: #bxc
                B = B ^ C
                flow.append("bxc")
            case 5: #out
                output.append(str(combo(ptr+1)%8))
                flow.append("out")
            case 6: #bdv
                B = A >> combo(ptr+1)
                flow.append("bdv")
            case 7: #cdv
                C = A >> combo(ptr+1)
                flow.append("cdv")

        ptr +=2
    return output

print(f"result part 1 : {",".join(solve(A))}")

# part 2
# found lower and upper limit by loop through rough large values and then narrowing down
lower = 35184372088832 # first A to get 16 digit output
upper = 281474976710656 # first A to get 17 digit output

# flow of control
"""
bst B =  a%8
bxl B = b ^ 2
cdv C = A >> b
adv A = A >> 3
bxl B = b ^ 7
bxc b = b ^ c
out B%8
jnz strat till a = 0

2,4, 1,2, 7,5 ,0,3 ,1,7 ,4,1 ,5,5 ,3,0
"""

def reverse_eng(program,ans):
    if not program: return ans
    for i in range(8):
        a = ans << 3 | i
        b = i ^ 2
        c = a >> b
        b = b ^ 7
        b = b ^ c
        if b%8 == program[-1]:
            sub = reverse_eng(program[:-1],a)
            if sub is None:continue
            return sub

print(f"part 2 result : {reverse_eng(program,0)}")
