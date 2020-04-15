from sympy import primefactors

seq = [1, 0]

for n in range(2, 520):

    seq.append(sum(sum(primefactors(k)) * seq[n - k]
                   for k in range(1, n + 1)) / n)

print(3**29)
print(int(seq[407]))
print(int(seq[-1]))
print(520 - 113)
print(primefactors(520 - 113))