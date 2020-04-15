def part_one(data):
    return(data.count('(') - data.count(')'))


def part_two(data):
    floor = 0
    for pos, char in enumerate(data, start=1):
        if char == '(':
            floor = floor + 1
        else:
            floor = floor - 1
            if floor < 0:
                return pos

with open('input.txt') as infile:
    data = infile.read()
print(part_one(data))
print(part_two(data))