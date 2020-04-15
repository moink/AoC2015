from collections import defaultdict
from functools import reduce
from operator import mul
from itertools import combinations_with_replacement

data = (
"""Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1""")

ingredients = {}
for line in data.splitlines():
    name, info = line.split(':')
    ingredients[name] = {}
    for inf in info.split(','):
        prop, val = inf.split()
        ingredients[name][prop] = int(val)


def calculate_value(contents):
    values = defaultdict(int)
    for ingredient in contents:
        for key, val in ingredients[ingredient].items():
            values[key] = values[key] + val
    for key, val in values.items():
        if val < 0:
            values[key] = 0
    calories = values.pop('calories')
    result = reduce(mul, values.values(), 1)
    return result, calories

results = []
for comb in combinations_with_replacement(ingredients.keys(), 100):
    val, cal = calculate_value(comb)
    if cal == 500:
        results.append(val)

print(max(results))