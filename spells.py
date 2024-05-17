class spells:
    def __init__(self,
                 spell_name: str,
                 damage: int = 1,
                 element: str = "Fire") -> None:
        self.spell_name = spell_name
        self.damage = damage
        self.element = element

    def __repr__(self):
        return f'{self.spell_name}'

    __str__ = __repr__


Fire_S = spells(spell_name= "Fireball",
              damage= 5,
              element= "Fire")
Water_S = spells(spell_name= "Bubble",
               damage= 5,
               element= "Water")
Moss_S = spells(spell_name= "Mossball",
              damage= 5,
              element= "Moss")

spellList = [
    Fire_S,
    Water_S,
    Moss_S,
]