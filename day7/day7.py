from functools import lru_cache

import numpy as np

connections = {}
with open('input.txt') as infile:
    lines = infile.readlines()
for line in lines:
    left, right = line.split(' -> ')
    connections[right.strip()] = left.split()

@lru_cache(None)
def evaluate(param):
    try:
        expr = connections[param]
    except KeyError:
        return np.ushort(param)
    if len(expr) < 2:
        return evaluate(expr[0])
    elif expr[0] == 'NOT':
        return ~evaluate(expr[1])
    elif expr[1] == 'AND':
        return evaluate(expr[0]) & evaluate(expr[2])
    elif expr[1] == 'OR':
        return evaluate(expr[0]) | evaluate(expr[2])
    elif expr[1] == 'LSHIFT':
        return evaluate(expr[0]) << int(expr[2])
    elif expr[1] == 'RSHIFT':
        return evaluate(expr[0]) >> int(expr[2])
    else:
        raise ValueError(expr)


print(evaluate('a'))
