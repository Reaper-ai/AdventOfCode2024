f = open("input","r")
data = f.read().split("\n")
reports = [list(map(int, i.split())) for i in data]

# part 1
unsafe = 0
for record in reports:
    sign = None
    for i in range(1,len(record)):
        k = record[i] - record[i-1]

        if abs(k) > 3 or abs(k) < 1:
            unsafe += 1
            break

        c_sign = k/abs(k) if k else 0
        if sign is None:
            sign = c_sign
        elif sign != c_sign:
            unsafe += 1
            break

print(f"result part 1 : {len(reports) - unsafe}")

# part 2
unsafe = 0
for record in reports:
    sign = None
    p = 0
    for i in range(1,len(record)):
        k = record[i] - record[i-1]

        if abs(k) > 3 or abs(k) < 1:
            p += 1
            continue

        c_sign = k/abs(k) if k else 0
        if sign is None:
            sign = c_sign
        elif sign != c_sign:
            p += 1

    if p > 1:
        unsafe +=1

print(f"result part 1 : {len(reports) - unsafe}")
