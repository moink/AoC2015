from collections import defaultdict
from itertools import permutations

with open('input.txt') as infile:
    lines = infile.readlines()

happiness = defaultdict(dict)

for line in lines:
    words = line[:-2].split()
    if words[2] == 'lose':
        happiness[words[0]][words[-1]] = -int(words[3])
    else:
        happiness[words[0]][words[-1]] = int(words[3])

def evaluate_total(order):
    total = 0
    for i in range(len(order) - 1):
        total = (total + happiness[order[i]][order[i+1]]
                 + happiness[order[i+1]][order[i]])
    # total = (total + happiness[order[0]][order[-1]] +
    #     #          happiness[order[-1]][order[0]])
    return total


totals = (evaluate_total(perm) for perm in permutations(happiness.keys()))
print(max(totals))