with open('input.txt') as infile:
    strings = infile.readlines()
count = 0
vowels = 'aeiou'
for string in strings:
    for i in range(len(string) - 2):
        first = string[i:i+2]
        rest = string[i+2:]
        if first in rest:
            for i in range(len(string)-2):
                if string[i] == string[i+2]:
                    count = count + 1
                    break
            break

print(count)