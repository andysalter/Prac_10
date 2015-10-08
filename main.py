"""
Game description:

Two armies go head to head in an all out, epic battle of honor to exclaim their superiority! Take on your friend
or the computer in this challenging (lol) battle for survival. Will you take your army to victory?

Mechanics:

This game has two players. Each has $20 to buy an army that can be composed of three different kinds of
fighter units: soldiers, archers, and cavalry. The following table gives a summary of each unit. The column
denoted by Fighter indicates the kind of fighter unit, Life the starting number of life points, Experience
the starting number of experience points, Speed the formula used to compute its speed, Damage on attack
the formula used to compute the damage it inflicts on attack, Lost life after defense the formula used to
compute the number of life points it loses after defending itself from the damage inflicted by another unit’s
attack, and the Cost for buying such a unit.

╔═════════╦══════╦════════════╦══════════════╦══════════════════╦═════════════════════════════════╦══════╗
║ Fighter ║ Life ║ Experience ║    Speed     ║ Damage on attack ║     Lost life after defence     ║ Cost ║
╠═════════╬══════╬════════════╬══════════════╬══════════════════╬═════════════════════════════════╬══════╣
║ Soldier ║    3 ║          0 ║ 1+experience ║ 1+experience     ║ if damage>experience: -1 life   ║    1 ║
║ Archer  ║    3 ║          0 ║ 3            ║ 1+experience     ║ -1 life                         ║    2 ║
║ Cavalry ║    4 ║          0 ║ 2            ║ 2*experience+1   ║ if damage>experience/2: -1 life ║    3 ║
╚═════════╩══════╩════════════╩══════════════╩══════════════════╩═════════════════════════════════╩══════╝


"""
from Menu import Menu
from combat import gladiatorialCombat as gladiatorialCombat
from player_setup import player_setup as player_setup

def start_game():
    print("Player 1 Setup:\n")
    player_1 = player_setup()

    print("Player 2 Setup:\n")
    player_2 = player_setup()

    print(combat_menu)
    selection = int(input())
    combat_select[selection](player_1, player_2)

def docs():
    print(__doc__)


main_menu = Menu("Select an option:", ["Start Game", "Help", "Quit"])
main_select = {1: start_game, 2: docs, 3: quit}

combat_menu = Menu("Select a combat mode:", ["Gladiatorial Combat"])
combat_select = {1: gladiatorialCombat}

while True:
    print(main_menu)
    selection = int(input())
    main_select[selection]()

