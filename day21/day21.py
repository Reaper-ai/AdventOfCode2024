from functools import cache

codes = open("input").read().split("\n")

keys = {'7': 0, '8': 1j, '9': 2j,
        '4': 1, '5': 1 + 1j, '6': 1 + 2j,
        '1': 2, '2': 2 + 1j, '3': 2 + 2j,
        '0': 3 + 1j, 'A': 3 + 2j}

pad = {"^": 1j, "A": 2j,
       "<": 1, "v": 1 + 1j, ">": 1 + 2j}

directions = {1: "v", -1: "^", 1j: ">", -1j: "<"}

def path(start,end,is_keypad):
    if is_keypad:
        invalid = 3
    else:
        invalid = 0

    rl = int(end.real - start.real)
    img = int(end.imag - start.imag)

    path = "<" * -img + "v" * rl + "^" * -rl + ">" * img

    if (start.real, end.imag) == (invalid,0) or (end.real, start.imag) == (invalid,0):
        path = path[::-1]

    return path + "A"
def mapper(all_seqs,graph):
    L = len(all_seqs)

    if len(graph) > 5:
        flag = True
    else:
        flag = False

    full_seq = ["" for _ in range(L)]
    for i in range(L):
        start = graph["A"]
        seq_to_typ = all_seqs[i]
        for button in seq_to_typ:
            end = graph[button]
            partial_seq = path(start, end,flag)
            full_seq[i] = "".join([full_seq[i],partial_seq])
            start = end

    return full_seq

# keypad -> Dpad1
input_seq = mapper(codes,keys)

# Dpad1 -> Dpad2
input_seq2 = mapper(input_seq,pad)
# Dpad2 -> Dpad3
input_seq3 = mapper(input_seq2,pad)

def res(input_seq):
    res = 0
    Q = len(input_seq)
    for i in range(Q):
        res += len(input_seq[i])*int(codes[i][:3])

    return res

print("part 1 result :", res(input_seq3))

# part 2

def path2(pad,invalid):
    look_up = {}

    for k in pad:
        for j in pad:
            start = pad[k]
            end = pad[j]
            rl = int(end.real - start.real)
            img = int(end.imag - start.imag)

            path = "<" * -img + "v" * rl + "^" * -rl + ">" * img

            if (start.real, end.imag) == (invalid,0) or (end.real, start.imag) == (invalid,0):
                path = path[::-1]

            look_up[(k,j)] = path + "A"

    return look_up
num_lookup = path2(keys,3)
Dpad_lookup = path2(pad,0)

@cache
def mapper2(seq, it,is_num=False):
    if it == 0:
        return len(seq)

    graph = num_lookup if is_num else Dpad_lookup
    g = keys if is_num else pad

    start = "A"
    len_seq = 0
    for button in seq:
        len_seq += mapper2(graph[(start, button)],it-1)
        start = button

    return len_seq


# part 2
res = 0
for code in codes:
    res  += mapper2(code,26,True)*int(code[:3])
print("part 2 result :", res)


