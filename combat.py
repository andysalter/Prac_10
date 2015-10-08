from player_setup import player_setup as player_setup


def gladiatorialCombat(army1, army2):
    while army1 > 0 and army2 > 0:
        army1_unit = army1.next_fighter()
        army2_unit = army2.next_fighter()

        if army1_unit.speed() == army2_unit.speed():
            army1_unit.defend(army2_unit.attack())
            army2_unit.defend(army1_unit.attack())

        elif army1_unit.speed() < army2_unit.speed():
            army1_unit.defend(army2_unit.attack())
            if army1_unit.isAlive():
                army2_unit.defend(army1_unit.attack())

        else:
            army2_unit.defend(army1_unit.attack())
            if army2_unit.isAlive():
                army1_unit.defend(army2_unit.attack())

        if army1_unit.isAlive() and army2_unit.isAlive():
            army1_unit.loseLife(1)
            army2_unit.loseLife(1)
        else:
            for unit in (army1_unit, army2_unit):
                if unit.isAlive():
                    unit.experience += 1

        if army1_unit.isAlive():
            army1.fighter_stack.push(army1_unit)

        if army2_unit.isAlive():
            army2.fighter_stack.push(army2_unit)

    if army1 == army2:
        print("Both armies have been annihilated! The game is a draw")

    else:
        winning_army = max(army1, army2)
        print('\n' + winning_army.player + ' has won the battle! Here stands his remaining victors!:\n')
        while not winning_army.fighter_stack.is_empty():
            print(winning_army.fighter_stack.pop())



print("Player 1 Setup:\n")
player_1 = player_setup()

print("Player 2 Setup:\n")
player_2 = player_setup()

gladiatorialCombat(player_1, player_2)