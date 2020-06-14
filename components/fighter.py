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
        selfName = self.owner.name.capitalize()
        targetName = target.name.capitalize()

        if damage > 0:
            target.fighter.take_damage(damage)
            results.append({"message": f"{selfName} attacks {targetName} for {damage} hit points."})
            results.extend(target.fighter.take_damage(damage))
        else:
            results.append({"message": f"{selfName} attacks {targetName} but deals no damage."})

        return results
