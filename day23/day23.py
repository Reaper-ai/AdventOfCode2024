from collections import defaultdict
from itertools import combinations
edges = [i.split("-") for i in open("input").read().split("\n")]
adj_list = defaultdict(list)
for edge in edges:
    f,t = edge
    adj_list[f].append(t)
    adj_list[t].append(f)


# part one
poss_connections = set()
for edge in adj_list:
    if edge[0] == "t":
        pairs = list(combinations(adj_list[edge], 2))
        for p in pairs:
            if p[1] in adj_list[p[0]]:
                poss_connections.add(tuple(sorted(p+(edge,))))

print("result part 1",len(poss_connections))


def find_clique():
    max_clique = []

    def expand(current_clique, candidates):
        nonlocal max_clique
        if not candidates:
            if len(current_clique) > len(max_clique):
                max_clique = current_clique[:]
            return

        for node in candidates[:]:  # Copy the list to avoid modification during iteration
            new_candidates = [neighbor for neighbor in adj_list[node] if neighbor in candidates]
            expand(current_clique + [node], new_candidates)
            candidates.remove(node)

    for node in adj_list:
        expand([node], adj_list[node])

    return max_clique

largest_clique = sorted(find_clique())
print("result part 2 ",*largest_clique,sep=",")
