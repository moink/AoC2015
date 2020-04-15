import scipy.signal

from util import load_grid, show_grid, draw_grid
import numpy as np

grid = load_grid('input.txt')
grid[0, 0] = 1
grid[0, -1] = 1
grid[-1, 0] = 1
grid[-1, -1] = 1
CONVOLVE_MATRIX = np.asarray([[1, 1, 1], [1, 0, 1], [1, 1, 1]])


def count_neighbours(state):
    result = scipy.signal.convolve2d(state, CONVOLVE_MATRIX, mode='same')
    return result


def one_step(state):
    counts = count_neighbours(state)
    result = np.where(np.logical_and(state == 1,
                                     np.logical_or(counts == 2,
                                                   counts == 3)), 1, 0)
    result = np.where(np.logical_and(state == 0, counts == 3), 1, result)
    result[0, 0] = 1
    result[0, -1] = 1
    result[-1, 0] = 1
    result[-1, -1] = 1
    return result

for _ in range(100):
    draw_grid(grid)
    grid = one_step(grid)

print(np.sum(grid))
show_grid(grid)
