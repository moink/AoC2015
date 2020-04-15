import numpy as np

presents = np.zeros((1000000), dtype=int)
for elf in range(1, 1000000):
    for j in range(elf, min(50*elf, 1000000), elf):
        presents[j] = presents[j] + elf * 11

print(min(np.argwhere(presents >= 36000000)))
