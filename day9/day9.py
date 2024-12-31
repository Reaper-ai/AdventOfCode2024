f = open("input","r")
data = "".join(f.read().split("\n"))

# part 1
long_disk = []
for i in range(len(data)):
    if i&1:
        long_disk += ["."]*int(data[i])
    else:
        long_disk += [str(i//2)]*int(data[i])

i, j = 0, len(long_disk)-1
while i < len(long_disk):
    if long_disk[i] == ".":
        if long_disk[j] != ".":
            long_disk[i], long_disk[j] = long_disk[j], long_disk[i]
            i +=1
            j -=1
        else:
            j-=1
    else:
        i +=1

result = 0
L = len(long_disk)
ind1 = long_disk.index(".")
frag1 = long_disk[:ind1]
long_disk.reverse()
ind2 = long_disk.index(".")
frag2 = long_disk[:ind2]
long_disk.reverse()
long_disk = frag1+frag2+long_disk[ind1:L-ind2]
for i in range(L):
    if not long_disk[i].isdigit():
        break

    result += int(long_disk[i])*i

print(f"result part 1 : {result}")

# part 2
result = 0
disk = []
class Node:
    def __init__(self,file,size):
        self.file = file
        self.size = size

for i in range(len(data)):
    if i&1:
        disk.append(Node(file = 0,size= int(data[i])))
    else:
        disk.append(Node(file = (i//2)+1,size= int(data[i])))

for i in range(len(disk)-1,-1,-1):
    for j in range(i):
        used = disk[i]
        free = disk[j]
        if used.file and not free.file and free.size >= used.size:

            disk[i] = Node(0, used.size)
            disk[j] = Node(0, free.size - used.size)
            disk.insert(j, Node(used.file, used.size))

long_disk = []
for node in disk:

    if node.size != 0:
        if node.file == 0:
            long_disk += ["."]*node.size
        else:
            long_disk += [str(node.file-1)]*node.size

for i,j in enumerate(long_disk):
    if j.isdigit():
        result += i*int(j)

print(f"result part 2 {result}")