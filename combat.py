


def gladiatorialCombat(army1, army2):
    """
    Complexity: O(n)
    When two units engage in an Encounter, their respective Speed is compared, and the unit with the greatest Speed attacks
    first, inflicting Damage. The defending unit then attempts to block the attack Damage. If incoming Damage > Defence,
    the block is unsuccessful, and the defender loses one Life point. If the defender is still alive, they attack and
    their opponent defends. If a unit dies, their killer gains one experience point.

    Each unit in the army will continue to fight until they have been killed or have brought their army to victory.
    At the end of an Encounter, if both units are still alive, they re-Encounter each other.
    """
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

    # if size of army1 = size of army2 = 0 then draw
    if army1 == army2:
        print("Both armies have been annihilated! The game is a draw")

    else:
        winning_army = max(army1, army2)
        print('\n' + winning_army.player + ' has won the battle! Here stands the remaining victors!:\n')
        while not winning_army.fighter_stack.is_empty():
            print(winning_army.fighter_stack.pop())