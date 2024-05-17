from weapons import Fist
from spells import spellList
from items import itemsList

elementTable = {
    "Water" : "Fire",
    "Fire"  : "Moss",
    "Moss"  : "Water",
}

class characters:
    def __init__(self,
                 name: str = ".",
                 health: int = 50) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = Fist
        self.spellList = spellList
        self.healItem = itemsList[0]

class Hero(characters):
    def __init__(self, name: str,
                 health: int = 10) -> None:
        super().__init__(name, health)

        self.default_spell = self.spellList[0]
        self.default_healItem = self.healItem
        self.superEffective = False
        self.uneffective = False

    def attack(self, monster):
        monster.health -= self.weapon.damage
        monster.health = max(monster.health, 0)

    def spellAttack(self, monster, choice: int):
        if monster.element == self.spellList[choice].element or monster.element == "Normal":
            monster.health -= self.spellList[choice].damage
            monster.health = max(monster.health, 0)
        elif elementTable[self.spellList[choice].element] == monster.element:
            monster.health -= self.spellList[choice].damage*2
            self.superEffective = True
            monster.health = max(monster.health, 0)
        elif elementTable[self.spellList[choice].element] != monster.element:
            monster.health -= self.spellList[choice].damage/2
            self.uneffective = True
            monster.health = max(monster.health, 0)

    def use_heal_item(self):
        if self.healItem.amount > 0:
            self.health += self.healItem.heal
            self.health = max(self.health, 0)
            self.healItem.amount -= 1
            print(f"{self.name} used a {self.healItem.name} and recovered {self.healItem.heal} health. \n {self.name} now has {self.health} health.")
        else:
            print(f"{self.name} has no more {self.healItem.name}")