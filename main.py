"""
Game description:

Two armies go head to head in an all out, epic battle of honor to exclaim their superiority! Take on your friend
or the computer in this challenging (lol) battle for survival. Will you take your army to victory?



Game-play:

This game has two players. Each has 20 gold to buy an army that can be composed of three different kinds of
fighter units: soldiers, archers, and cavalry. At the start of the game, each player sets up their army by choosing
the number of each fighter units they would like to purchase. After setting up each army, the players must agree
to a Combat Mode. At the beginning of the battle, Soldiers are positioned at the front, Archers in the middle, and the
Cavalry at the rear. The first two units then engage in an Encounter. When a unit dies, the next unit takes their place
and engages with their opponent. The action of a fighter that has survived an Encounter depends on the Combat Mode.
The battle continues in this fashion until one or both of the armies have been annihilated.

When two units engage in an Encounter, their respective Speed is compared, and the unit with the greatest Speed attacks
first, inflicting Damage. The defending unit then attempts to block the attack Damage. If incoming Damage > Defence,
the block is unsuccessful, and the defender loses one Life point. If the defender is still alive, they attack and
their opponent defends. If a unit dies, their killer gains one experience point.

If the speeds of the two units are identical, then both attack at the same time.



Combat Modes:

    * Gladiatorial Combat:
    Each unit in the army will continue to fight until they have been killed or have brought their army to victory.
    At the end of an Encounter, if both units are still alive, they re-Encounter each other.

    * More modes to be added soon...


Attributes:

    * Life:
    The vitality of a unit. Once this reaches zero, the unit endures an agonising death. See Mechanics for starting
    life

    * Experience:
    Experience is a measure of expertise and finesse. See mechanics for how this affects other attributes.

    * Speed:
    Experience is a measure of the agility of a unit. A unit with a greater Speed is able to attack before
    their opponent!

    * Damage
    When a unit attacks, they inflict Damage. Depending on the defencive capabilities of the defender, the defender
    may lose a Life point. See mechanics.

    * Defence
    A measure of the defencive capabilities of a unit. See mechanics.



Fighter Classes:

This game has two players. Each has 20 gold to buy an army that can be composed of three different kinds of
fighter units: soldiers, archers, and cavalry. The following table gives a summary of each unit's starting
attributes and their cost in gold.

╔═════════╦══════╦════════════╦══════════════╦══════════════════╦═════════════════════════════════╦══════╗
║ Unit    ║ Life ║ Experience ║    Speed     ║      Damage      ║              Defence            ║ Cost ║
╠═════════╬══════╬════════════╬══════════════╬══════════════════╬═════════════════════════════════╬══════╣
║ Soldier ║    3 ║          0 ║ 1+experience ║ 1+experience     ║ experience                      ║    1 ║
║ Archer  ║    3 ║          0 ║ 3            ║ 1+experience     ║ 0                               ║    2 ║
║ Cavalry ║    4 ║          0 ║ 2            ║ 2*experience+1   ║ experience/2                    ║    3 ║
╚═════════╩══════╩════════════╩══════════════╩══════════════════╩═════════════════════════════════╩══════╝



"""
from menu import Menu
from combat import gladiatorialCombat

from player_setup \
    import player_setup as player_setup, random_army as random_army

def go_main_menu():
    print(main_menu)
    selection = int(input())
    main_select[selection]()


def start_game():
    # select PvP or PvE
    print(player_menu)
    selection = int(input())
    player_mode = player_select[selection]

    # setup player 1
    print("Player 1 Setup:\n")
    player_1 = player_setup()   # assigns tuple (name, n_soldiers, n_archers, n_cavalry)

    if player_mode == 'PvP':
        print("Player 2 Setup:\n")
        player_2 = player_setup()
    else:
        # if PvE create random army
        player_2 = random_army()
        print('\nEnemy Army:',
              '\tSoldiers: '+str(player_2[1]),
              '\tArchers: '+str(player_2[2]),
              '\tCavalrymen: '+str(player_2[3]), sep='\n')

    print(combat_menu)
    selection = int(input())
    combat_select[selection](player_1, player_2)



    go_main_menu()


def docs():
    print(__doc__)
    back = input("Press 'ENTER' to return to Main Menu")
    if back == '':
        go_main_menu()


# initialise menus
main_menu = Menu("Select an option:", ["Start Game", "Help", "Quit"])
main_select = {1: start_game, 2: docs, 3: quit}

combat_menu = Menu("Select a combat mode:", ["Gladiatorial Combat"])
combat_select = {1: gladiatorialCombat}

player_menu = Menu("Select a player mode:", ['PvP', 'PvE'])
player_select = {1: 'PvP', 2: 'PvE'}


# go to main menu
go_main_menu()