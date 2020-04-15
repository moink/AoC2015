from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul


def part_1():
    solve_problem(3)


def part_2():
    solve_problem(4)


def solve_problem(parts):
    with open('input.txt') as infile:
        weights = [int(line) for line in infile.readlines()]
    goal_sum = sum(weights) // parts
    results = []
    for num_vals in range(1, len(weights) // parts):
        for combo in combinations(weights, num_vals):
            if sum(combo) == goal_sum:
                quantum = reduce(mul, combo)
                results.append(quantum)
    print(results)
    print(min(results))


def find_sums(weights):
    sums = set()
    for a in weights:
        for b in weights:
            if (a + b) in weights:
                lesser = min(a, b)
                greater = max(a, b)
                sums.add((lesser, greater, lesser + greater))
    print(sums)
    print(len(sums))


if __name__ == '__main__':
    part_2()
