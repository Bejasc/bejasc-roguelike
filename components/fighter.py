import tcod as libtcod
from game_messages import Message


class Fighter:
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power

    def take_damage(self, amount):
        results = []
        self.hp -= amount
        if self.hp <= 0:
            results.append({"dead": self.owner})

        return results

    def attack(self, target):
        results = []

        damage = self.power - target.fighter.defense

        if damage > 0:
            target.fighter.take_damage(damage)
            results.append({"message": Message(f"{self.owner.name} attacks {target.name} for {damage} hit points.", libtcod.white)})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({"message": Message(f"{self.owner.name} attacks {target.name} but deals no damage.", libtcod.white)})

        return results