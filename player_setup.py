from Army import Army


def player_setup():
    name = input("\tEnter your name: ")
    gold = 20
    n_soldiers = 0
    n_archers = 0
    n_cavalry = 0

    while True:
        try:
            n_soldiers = int(input("\tHow many soldiers would you like?: "))
            if n_soldiers < 0:
                raise ValueError
        except ValueError:
            print("\t!! Invalid input. Must be a natural number.")
            continue

        if gold - n_soldiers < 0:
            print("\t!! Not enough funds.")
            continue

        gold -= n_soldiers
        break

    while True and gold > 0:
        try:
            n_archers = int(input("\tHow many archers would you like?: "))
            if n_archers < 0:
                raise ValueError
        except ValueError:
            print("\t!! Invalid input. Must be a natural number.")
            continue

        if gold - (n_archers * 2) < 0:
            print("\t!! Not enough funds.")
            continue

        gold -= n_archers * 2
        break

    while True and gold > 0:
        try:
            n_cavalry = int(input("\tHow many cavalrymen would you like?: "))
            if n_cavalry < 0:
                raise ValueError
        except ValueError:
            print("\t!! Invalid input. Must be a natural number.")
            continue

        if gold - (n_cavalry * 3) < 0:
            print("\t!! Not enough funds.")
            continue

        gold -= n_cavalry * 3
        break

    return Army(name, n_soldiers, n_archers, n_cavalry)




