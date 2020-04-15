import json

def sum_values(data):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(sum_values(item) for item in data)
    elif isinstance(data, dict):
        if 'red' in data.values():
            return 0
        else:
            return sum(sum_values(item) for item in data.values())
    else:
        return 0

with open('input.txt') as infile:
    data = json.load(infile)
print(sum_values(data))