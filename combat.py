from Army import gladiator_army


def combat(unit1, unit2):
    """
    Complexity: O(n)
    When two units engage in an Encounter, their respective Speed is compared, and the unit with the greatest Speed attacks
    first, inflicting Damage. The defending unit then attempts to block the attack Damage. If incoming Damage > Defence,
    the block is unsuccessful, and the defender loses one Life point. If the defender is still alive, they attack and
    their opponent defends. If a unit dies, their killer gains one experience point.

    Each unit in the army will continue to fight until they have been killed or have brought their army to victory.
    At the end of an Encounter, if both units are still alive, they re-Encounter each other.
    """

    if unit1.speed() == unit2.speed():
        unit1.defend(unit2.attack())
        unit2.defend(unit1.attack())

    elif unit1.speed() < unit2.speed():
        unit1.defend(unit2.attack())
        if unit1.isAlive():
            unit2.defend(unit1.attack())

    else:
        unit2.defend(unit1.attack())
        if unit2.isAlive():
            unit1.defend(unit2.attack())

    if unit1.isAlive() and unit2.isAlive():
        unit1.loseLife(1)
        unit2.loseLife(1)
    else:
        for unit in (unit1, unit2):
            if unit.isAlive():
                unit.experience += 1

    return unit1, unit2


def gladiatorialCombat(player1, player2):
    print("The battle begins!")
    p1_army = gladiator_army(*player1)
    p2_army = gladiator_army(*player2)

    while p1_army > 0 and p2_army > 0:
        p1_unit = p1_army.next_fighter()
        p2_unit = p2_army.next_fighter()
        units = combat(p1_unit, p2_unit)

        if units[0].isAlive():
            p1_army.fighter_stack.push(units[0])

        if units[1].isAlive():
            p2_army.fighter_stack.push(units[1])

    if p1_army == p2_army:
        print("Both armies have been annihilated! The game is a draw")

    else:
        winning_army = max(p1_army, p2_army)
        print('\n' + winning_army.player + ' has won the battle! Here stands the remaining victors!:\n')
        while not winning_army.fighter_stack.is_empty():
            print(winning_army.fighter_stack.pop())