class Items:
    def __init__(self,
                 name: str,
                 amount: int = 1) -> None:
        self.name = name
        self.amount = amount
    def __repr__(self):
        return f"{self.name}"
    __str__ = __repr__

    def use_item(self, player):
        print("Not done")

class healItems(Items):
    def __init__(self,
                name: str,
                heal: int = 5,
                amount: int = 1) -> None:
        super().__init__(name)
        self.heal = heal
        self.amount = amount
    
    def use_heal_item(self, player, item):
        if item.amount > 0:
            player.health += item.heal
            player.health = max(player.health, 0)
            item.amount -= 1
            print(f"{player.name} used a {item.name} and recovered {item.heal} health. \n {player.name} now has {player.health} health.")
        else:
            print(f"{player.name} has no more {item.name}")

potion = healItems(name= "Potion",
                   heal= 5,
                   amount= 4)

potionSuper = healItems(name= "Super Potion",
                        heal = 10,
                        amount= 2)

healItemslist = [
    potion,
    potionSuper
]

Dragon_Killer = Items(name= "Dragon Killer",
                      amount= 1)

itemsList = [
 Dragon_Killer
]

