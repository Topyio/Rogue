from character import characters
from weapons import monsterWeaponlist,bossWeaponlist

class Monster:
    def __init__(self,
                 name: str, 
                 health: int = 10,
                 element: str = "Water"
                 ) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = monsterWeaponlist[0]
        self.element = element

    def monster_attack(self, Hero):
        Hero.health -= self.weapon.damage
        Hero.health = max(Hero.health, 0)

class Slime(Monster):
    def __init__(self, name: str = "Slime",
                  health: int = 10,
                  element: str = "Water") -> None:
        super().__init__(name, health, element)

class Chicken(Monster):
    def __init__(self, 
                name: str = "Clucky The Chicken",
                health: int = 10, 
                element: str = "Normal") -> None:
        super().__init__(name, health, element)
        self.weapon = monsterWeaponlist[1]

SL = Slime()
CH = Chicken()
monsterList = [
    SL,
    CH
]

class Dragon(Monster):
    def __init__(self, 
                name: str = "Dragon",
                health: int = 50,
                element: str = "Fire") -> None:
        super().__init__(name, health, element)
        self.weapon = bossWeaponlist[0]

Dra = Dragon()
bossMonsterlist = [
    Dra
]
