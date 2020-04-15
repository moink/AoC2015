from collections import defaultdict

data =(
"""Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
Cupid can fly 22 km/s for 2 seconds, but then must rest for 41 seconds.
Rudolph can fly 11 km/s for 5 seconds, but then must rest for 48 seconds.
Donner can fly 28 km/s for 5 seconds, but then must rest for 134 seconds.
Dasher can fly 4 km/s for 16 seconds, but then must rest for 55 seconds.
Blitzen can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Prancer can fly 3 km/s for 21 seconds, but then must rest for 40 seconds.
Comet can fly 18 km/s for 6 seconds, but then must rest for 103 seconds.
Vixen can fly 18 km/s for 5 seconds, but then must rest for 84 seconds.""")

# data = (
# # """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""
# # )

def calc_dist(time, line):
    words = line.split()
    name = words[0]
    speed = int(words[3])
    fly_time = int(words[6])
    rest_time = int(words[-2])
    full_sprints = time // (fly_time + rest_time)
    leftover = time % (fly_time + rest_time)
    result = full_sprints * speed * fly_time + speed * (min(leftover, fly_time))
    return name, result

time = 0
result = defaultdict(int)
while time < 2504:
    time = time + 1
    best_dist = 0
    winners = []
    for line in data.splitlines():
        key, val = calc_dist(time, line)
        if val > best_dist:
            best_dist = val
            winners = [key]
        elif val == best_dist:
            winners.append(key)
    for winner in winners:
        result[winner] += 1
print(max(result.values()))
print(sum(result.values()))
print(result)