with open('input.txt') as infile:
    data = infile.readlines()

stuff = {}
for line in data:
    sue, things = line.split(':', 1)
    _, suenum = sue.split(' ')
    stuff[int(suenum)] = {}
    for thing in things.split(','):
        name, num = thing.split(':')
        stuff[int(suenum)][name.strip()] = int(num)

to_match = (
"""children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
)

match = {}
for line in to_match.splitlines():
    name, num = line.split(':')
    match[name] = int(num)


for sue_num, sue_stuff in stuff.items():
    found = True
    for name, num in sue_stuff.items():
        if name in ['cats', 'trees']:
            if match[name] >= num:
                found = False
        elif name in ['pomeranians', 'goldfish']:
            if match[name] <= num:
                found = False
        elif match[name] != num:
            found = False
            break
    if found:
        print(sue_num)
        break