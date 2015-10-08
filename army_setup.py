from Army import Army

def player_setup():
    name = input("\tEnter your name: ")

    n_soldiers = int(input("How many soldiers would you like?: "))
    n_archers = int(input("How many archers would you like?: "))
    n_cavalry = int(input("How many cavalrymen would you like?: "))

    return Army(name, n_soldiers, n_archers, n_cavalry)


print("Player 1 Setup:\n")
P1_army = player_setup()

print("Player 2 Setup:\n")
P2_army = player_setup()

