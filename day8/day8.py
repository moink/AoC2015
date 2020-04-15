
def main():
    with open('input.txt') as infile:
        lines = infile.readlines()
    count = 0
    for line in lines:
        count = count + count_size(line)
    print(count)


def count_size(line):
    line = line.replace('\n', '')
    string = eval(line.strip())
    full_len = 2 + len(line) + line.count('\\') + line.count('"')
    return full_len - len(line)


main()
