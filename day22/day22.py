"""Day 22"""

import abc
from itertools import combinations_with_replacement, product

LARGE_NUMBER = 999999999

class Spell(abc.ABC):

    def __init__(self, caster, enemy):
        self.caster = caster
        self.enemy = enemy

    @property
    @abc.abstractmethod
    def cost(self):
        pass

    @abc.abstractmethod
    def apply_effect(self):
        pass

    def __bool__(self):
        return False

class Effect(Spell):

    def __init__(self, caster, enemy):
        super().__init__(caster, enemy)
        self.time_remaining = self.duration

    @property
    @abc.abstractmethod
    def duration(self):
        pass

    def remove_effect(self):
        pass

    def clock_tick(self):
        self.time_remaining = self.time_remaining - 1
        if self.time_remaining >= 0:
            self.apply_effect()
        else:
            self.remove_effect()

    def __bool__(self):
        return self.time_remaining > 0


    def __hash__(self):
        return hash(type(self).__name__)


    def __eq__(self, other):
        return type(self) == type(other)

class Shield(Effect):

    cost = 113
    duration = 5

    def apply_effect(self):
        self.caster.armor = 7

    def remove_effect(self):
        self.caster.armor = 0


class Poison(Effect):
    cost = 173
    duration = 6

    def apply_effect(self):
        self.enemy.apply_damage(3)


class Recharge(Effect):

    cost = 229
    duration = 5

    def apply_effect(self):
        self.caster.add_mana(101)

class Drain(Spell):

    cost = 73
    duration = 5

    def apply_effect(self):
        self.caster.apply_damage(-2)
        self.enemy.apply_damage(2)


class Character(abc.ABC):

    @property
    @abc.abstractmethod
    def hit_points(self):
        pass

    def __init__(self):
        self.health = self.hit_points
        self.effects = []

    def apply_damage(self, damage):
        true_damage = max(1, damage - self.armor)
        self.health = self.health - true_damage

    def heal(self, heal_points):
        self.health = self.health + heal_points

    def add_effect(self, spell):
        self.effects.append(spell)

    def remove_effect(self, spell):
        self.effects.remove(spell)

    @property
    @abc.abstractmethod
    def armor(self):
        pass

    def __bool__(self):
        return self.health > 0

class Wizard(Character):

    hit_points = 50
    # hit_points = 10
    mana_pool = 500
    # mana_pool = 250
    base_armor = 0
    armor = 0

    def __init__(self):
        super().__init__()
        self.mana = self.mana_pool
        self.armor = self.base_armor

    def add_mana(self, mana_amount):
        self.mana = self.mana + mana_amount

    def cast_spell(self, spell):
        self.mana = self.mana - spell.cost
        if self.mana < 0:
            raise ValueError('Out of mana')

class Boss(Character):

    hit_points = 51
    damage = 9
    # hit_points = 14
    # damage = 8
    armor = 0

def apply_effects(effects):
    result = effects.copy()
    for effect in effects:
        if effect:
            effect.clock_tick()
        if not effect:
            result.remove(effect)
    return result


class Magic_Missile(Spell):

    helpful = False
    cost = 53
    def apply_effect(self):
        self.enemy.apply_damage(4)


class Drain(Spell):

    helpful = True
    cost = 73
    def apply_effect(self):
        self.caster.heal(2)
        self.enemy.apply_damage(2)


def run_fight(spell_sequence):
    player = Wizard()
    boss = Boss()
    mana_spent = 0
    effects = set()
    while player and boss:
        # Player turn
        try:
            spell_name = next(spell_sequence)
        except StopIteration:
            return False, mana_spent
        spell_class = globals()[spell_name]
        spell = spell_class(player, boss)
        player.health = player.health - 1
        if player.health <= 0:
            return False, mana_spent
        player.armor = 0
        effects = apply_effects(effects)
        try:
            player.cast_spell(spell)
        except ValueError:
            return False, mana_spent
        mana_spent = mana_spent + spell.cost
        if isinstance(spell, Effect):
            effects.add(spell)
        else:
            spell.apply_effect()
        # Boss turn
        effects = apply_effects(effects)
        if boss:
            player.apply_damage(boss.damage)
    if boss:
        return False, mana_spent
    return True, mana_spent

def main():
    avail_spells = ('Recharge', 'Shield', 'Drain', 'Poison', 'Magic_Missile')
    # bad_sequence = ('Recharge', 'Poison', 'Shield', 'Magic_Missile', 'Poison',
    #                 'Magic_Missile', 'Magic_Missile', 'Magic_Missile')
    # won, mana_spent = run_fight(iter(bad_sequence))
    # print(won, mana_spent)
    win_costs = []
    for num_spells in range(9):
    # num_spells = 8
    # print(5**num_spells)
        combo = product(avail_spells, repeat=num_spells)
        # # print(len(list(combo)))
        for spell_sequence in combo:
        #     # print(spell_sequence)
            won, mana_spent = run_fight(iter(spell_sequence))
            if won:
                # print(spell_sequence)
                win_costs.append(mana_spent)
        print(f'{num_spells} : {len(win_costs)}')
    print(min(win_costs))

if __name__ == '__main__':
    main()