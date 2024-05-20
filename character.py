from weapons import Fist
from spells import spellList
from items import itemsList,healItemslist
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
        self.itemsList = itemsList
        self.healList = healItemslist

class Hero(characters):
    def __init__(self, name: str,
                 health: int = 10) -> None:
        super().__init__(name, health)
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

    def use_heal_item(self, choice: int):
        if self.healList[choice].amount > 0:
            self.health += self.healList[choice].heal
            self.health = max(self.health, 0)
            self.healList[choice].amount -= 1
            print(f"{self.name} used a {self.healList[choice].name} and recovered {self.healList[choice].heal} health. \n{self.name} now has {self.health} health.")
        else:
            print(f"{self.name} has no more {self.healList[choice].name}")
    
    def use_item(self, choice: int, monster):
        if self.itemsList[choice].amount > 0:
            if self.itemsList[choice].name == "Dragon Killer":
                if monster.name == "Dragon":
                    monster.health = 0
                    print("The Dragon Killer obliterates the Dragon (cheater)")
                else:
                    print("Item has no effect")