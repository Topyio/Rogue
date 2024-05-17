class weapon:
    def __init__(self,
                 weapon_name: str,
                 damage: int = 1,
                 value: int = 0) -> None:
        self.weapon_name = weapon_name
        self.damage = damage
        self.value = value

Fist = weapon(weapon_name= "Fists",
              damage= 5)

playerWeaponslist = [
    Fist
]
class monsterWeapon(weapon):
    def __init__(self, weapon_name: str, damage: int = 1, value: int = 0) -> None:
        super().__init__(weapon_name, damage, value)
Slime_ball = monsterWeapon(weapon_name= "Slime Ball",
                   damage= 2)

Claw = monsterWeapon(weapon_name= "Claw",
              damage= 3)

Dragon_Breath = monsterWeapon(weapon_name= "Dragon Breath",
                              damage= 5)

monsterWeaponlist = [
    Slime_ball,
    Claw
]

bossWeaponlist = [
    Dragon_Breath
]