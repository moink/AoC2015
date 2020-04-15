from itertools import groupby

value = '1113222113'
for _ in range(50):
    value = ''.join(
        [str(len(list(g))) + str(k) for k, g in groupby(value)])
print(len(value))

# 3579240 is too low
# 7179592 is too high