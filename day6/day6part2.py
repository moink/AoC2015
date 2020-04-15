import numpy as np
import re

grid = np.zeros((1000, 1000), dtype=int)
with open('input.txt') as infile:
    strings = infile.readlines()
for instruction in strings:
    before, between, after = instruction.split(',')
    x1, y1, x2, y2 = (int(x) for x in re.findall(r'\d+', instruction))
    if instruction.startswith('turn on'):
        grid[x1:x2+1, y1:y2+1] = grid[x1:x2+1, y1:y2+1] + 1
    elif instruction.startswith('turn off'):
        grid[x1:x2+1, y1:y2+1] = np.maximum(grid[x1:x2+1, y1:y2+1] - 1, 0)
    else: #toggle
        grid[x1:x2+1, y1:y2+1] = grid[x1:x2+1, y1:y2+1] + 2
print(np.sum(grid))

