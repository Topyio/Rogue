import random
import os
from character import Hero
from battle import Battle
from monster import monsterList,bossMonsterlist

player = Hero(name = "█")

Game = Battle()

gameLoop = False
battleLoop = False

#intro
print("What is you're name, hero?")
player.name = str(input())
os.system("cls")
print("Nice name!")
input()
os.system("cls")
print(f"Have fun exploring the dungeon {player.name}!")
input()

#Game loop
while not gameLoop:

    while not battleLoop:
        if not Game.Monster_defeated >= 3:
            Game.Encounter(random.choice(monsterList),player)
            input()
        else:
            battleLoop = True
    
    print(f"{player.name} has killed {Game.Monster_defeated} monsters. \nYou now approach the scourge of the dungeon.")
    input()
    os.system("cls")
    print("Prepare yourself.")
    input()
    Game.Encounter(bossMonsterlist[0],player)
    gameLoop = True

#End
print(f"Good job, {player.name}! You've defeated the scourge of the dungeon!")
input()
quit()