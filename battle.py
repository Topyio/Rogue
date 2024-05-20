import os
import random
from items import healItemslist
class Battle:
    def __init__(self) -> None:
        self.GameOver = False
        self.Monster_defeated = 0
        self.ran_away = False

    def Encounter(self, monster, player):
        print(f"{player.name} encountered a {monster.name}")
        while monster.health > 0:
            print(f"What will {player.name} do? \n 1-Attack 2-Spell 3-Item 4-Run")
            choice = int(input())
            if choice == 1:
                player.attack(monster)
                print(f"{player.name} has dealt {player.weapon.damage} damage to {monster.name} with {player.weapon.weapon_name} \n{monster.name} has {monster.health} health left.")
            if choice == 2:
                print(f"Choose a spell(1,2,3...etc): {player.spellList}")
                spellChoice = int(input())-1
                player.spellAttack(monster,spellChoice)
                if player.superEffective == True:
                    print(f"{player.name} has dealt {player.spellList[spellChoice].damage*2} super effective damage to {monster.name} with {player.spellList[spellChoice]}\n{monster.name} has {monster.health} health left.")
                    player.superEffective = False
                elif player.uneffective == True:
                    print(f"{player.name} has dealt {player.spellList[spellChoice].damage/2} uneffective damage to {monster.name} with {player.spellList[spellChoice]}\n{monster.name} has {monster.health} health left.")
                    player.uneffective = False
                else:
                     print(f"{player.name} has dealt {player.spellList[spellChoice].damage} damage to {monster.name} with {player.spellList[spellChoice]}\n{monster.name} has {monster.health} health left.")
            if choice == 3:
                print("Battle Item(1) or Heal Item(2)")
                itemListchoice = (input())
                if itemListchoice == "1":
                    print(f"Choose a Battle Item:\n {player.itemsList}")
                    itemChoice = int(input())-1
                    player.use_item(itemChoice,monster)
                elif itemListchoice == "2":
                    print(f"Choose a Heal Item:\n {player.healList}")
                    healItemchoice = int(input()) -1
                    player.use_heal_item(healItemchoice)
                elif itemListchoice == "back":
                    return
            if choice == 4:
                running = random.randint(0,20)
                if running >= 6:
                    print(f"{player.name} couldn't run away.")
                else:
                    print(f"{player.name} tries to run!")
                    self.ran_away = True
                    monster.health = 0
            if monster.health > 0:
                monster.monster_attack(player)
                print(f"{monster.name} has dealt {monster.weapon.damage} damage to {player.name} \n{player.name} has {player.health} health left.")
            if player.health == 0:
                print("Game over")
                quit()
            
            input()
            os.system("cls")
        if monster.health <= 0 and self.ran_away == False:
            print(f"{player.name} defeated the {monster.name}!")
            monster.health = monster.max_health
            self.Monster_defeated += 1
        elif monster.health <= 0 and self.ran_away == True:
            print(f"{player.name} ran away")
            monster.health = monster.max_health
            self.ran_away = False