
f = open("input", "r")
data = f.read().split("\n")


# part 1
def transpose(data):
    data = [list(i) for i in data]
    tdata = [[data[j][i] for j in range(len(data[0]))] for i in range(len(data))]
    tdata = ["".join(i) for i in tdata]
    return tdata

def search_diagonally(grid, sub):
    rows = len(grid)
    cols = len(grid[0])
    sub_len = len(sub)
    count = 0

    for i in range(rows):
        for j in range(cols):
            # main diag
            if i + sub_len <= rows and j + sub_len <= cols:
                if all(grid[i + k][j + k] == sub[k] for k in range(sub_len)):
                    count += 1
            # sec diag
            if i - sub_len >= -1 and j + sub_len <= cols:
                if all(grid[i - k][j + k] == sub[k] for k in range(sub_len)):
                    count += 1
    return count
result = 0
h_v_xmas = lambda data: sum(i.count("XMAS") + i.count("SAMX") for i in data)
result += (h_v_xmas(data) + h_v_xmas(transpose(data)))
result += search_diagonally(data,"XMAS")
result += search_diagonally(data,"SAMX")

print(f"result part 1 : {result}")


# part 2
result = 0
for i in range(1,len(data)-1):
    for j in range(1,len(data[0])-1):
        if data[i][j] == "A":
            if data[i-1][j-1] =="M" and data[i-1][j+1] == "M" and data[i+1][j+1] == "S" and data[i+1][j-1] == "S":
                result += 1
            if data[i - 1][j - 1] == "M" and data[i - 1][j + 1] == "S" and data[i + 1][j + 1] == "S" and data[i + 1][j - 1] == "M":
                result += 1
            if data[i-1][j-1] =="S" and data[i-1][j+1] == "M" and data[i+1][j+1] == "M" and data[i+1][j-1] == "S":
                result += 1
            if data[i-1][j-1] =="S" and data[i-1][j+1] == "S" and data[i+1][j+1] == "M" and data[i+1][j-1] == "M":
                result += 1

print(f"result part 2 : {result}")