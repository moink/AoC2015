from itertools import combinations
eggnog = 150
containers = [50, 44, 11, 49, 42, 46, 18, 32, 26, 40, 21, 7, 18, 43, 10, 47,
              36, 24, 22, 40]

# eggnog = 25
# containers = [20, 15, 10, 5, 5]

for n in range(1, len(containers) + 1):
    num_ways = sum(1 for comb in combinations(containers, n)
                   if sum(comb) == eggnog)
    if num_ways > 0:
        print(num_ways)
        break