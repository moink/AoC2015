with open('input.txt') as infile:
    strings = infile.readlines()
count = 0
vowels = 'aeiou'
for string in strings:
    if 'ab' in string or 'cd' in string or 'pq' in string or 'xy' in string:
        continue
    if sum(1 for char in string if char in vowels) < 3:
        continue
    count = count + any(char == string[i+1]
                        for i, char in enumerate(string[ :-1]))
print(count)