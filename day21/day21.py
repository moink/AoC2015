import pandas as pd
import itertools

boss_stats = {'hit': 100, 'damage': 8, 'armor': 2}
avail = pd.read_csv('armor.csv')

def simulate_fight(stats):
    boss_health = boss_stats['hit']
    my_health = stats['hit']
    boss_damage = max(1, boss_stats['damage'] - stats['armor'])
    my_damage = max(1, stats['damage'] - boss_stats['armor'])
    while boss_health > 0 and my_health > 0:
        boss_health = boss_health - my_damage
        if boss_health <= 0:
            break
        my_health = my_health - boss_damage
    if my_health > 0:
        return True
    return False

def sum_armour(wearing):
    result = avail.loc[wearing, :].sum()
    result['hit'] = 100
    return result

def get_vals(wearing):
    stats = sum_armour(wearing)
    win = simulate_fight(stats)
    return win, stats['cost']

def generate_combinations():
    weapons = range(5)
    # armor = itertools.chain(range(5, 10), [17])
    armor = range(5, 10)
    rings = itertools.chain.from_iterable(
        (itertools.combinations(range(10, 16), n) for n in range(3)))
    for combo in itertools.product(weapons, armor, rings):
        result = []
        for tup in combo:
            if isinstance(tup, tuple):
                for elem in tup:
                    result.append(elem)
            else:
                result.append(tup)
        yield result

win_costs = []
lose_costs = []
for combo in generate_combinations():
    win, cost = get_vals(combo)
    if win:
        win_costs.append(cost)
    else:
        lose_costs.append(cost)
print(min(win_costs))
print(max(win_costs))
print(min(lose_costs))
print(max(lose_costs))
# 146 is too low
#356 is too high
print(get_vals([4, 5, 12, 13]))
print(avail.shape)