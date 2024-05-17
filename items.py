class Items:
    def __init__(self,
                 name: str,) -> None:
        self.name = name
    def __repr__(self):
        return f"{self.name}"
    __str__ = __repr__

class healItems(Items):
    def __init__(self,
                name: str,
                heal: int = 5,
                amount: int = 1) -> None:
        super().__init__(name)
        self.heal = heal
        self.amount = amount
    
    def use_heal_item(self, player):
        if self.amount > 0:
            player.health += self.heal
            player.health = max(player.health, 0)
            self.amount -= 1
            print(f"{player.name} used a {healItems.name} and recovered {healItems.heal} health. \n {player.name} now has {player.health} health.")
        else:
            print(f"{player.name} has no more {healItems.name}")

potion = healItems(name= "Potion",
                   heal= 5,
                   amount= 3)

itemsList = [
    potion,
]