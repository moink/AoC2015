with open('input.txt') as infile:
    data = infile.readlines()
paper_needed = 0
ribbon_needed = 0
for line in data:
    dimensions = sorted(int(num) for num in line.split('x'))
    smallest_area = dimensions[0] * dimensions[1]
    paper_needed = paper_needed + smallest_area + 2*(
        smallest_area + dimensions[0] * dimensions[2]
        + dimensions[1] * dimensions[2])
    ribbon_needed = (ribbon_needed +
        dimensions[0] * dimensions[1] *dimensions[2]
        + 2 * (dimensions[0] + dimensions[1]))
print(paper_needed)
print(ribbon_needed)