from itertools import permutations
from collections import defaultdict

with open('input.txt') as infile:
    lines = infile.readlines()
distances = defaultdict(dict)
for line in lines:
    names, dist = line.split(' = ')
    name1, name2 = names.split(' to ')
    distances[name1][name2] = int(dist)
    distances[name2][name1] = int(dist)
counts = []
for perm in permutations(distances.keys()):
    count = 0
    for i in range(len(perm) - 1):
        count = count + distances[perm[i]][perm[i+1]]
    counts.append(count)
print(max(counts))