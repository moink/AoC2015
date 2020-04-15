def evaluate_char(x, y, char):
    if char == '>':
        x = x + 1
    elif char == '<':
        x = x - 1
    elif char == '^':
        y = y + 1
    elif char == 'v':
        y = y - 1
    return x, y


with open('input.txt') as infile:
    data = infile.read()
delivered = {(0, 0)}
x_s = 0
x_r = 0
y_s = 0
y_r = 0
for char_s, char_r in zip(*[iter(data)]*2):
    x_s, y_s = evaluate_char(x_s, y_s, char_s)
    delivered.add((x_s, y_s))
    x_r, y_r = evaluate_char(x_r, y_r, char_r)
    delivered.add((x_r, y_r))
print(len(delivered))