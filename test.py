from Army import Army
from Fighter import *


army1_unit = Soldier()
army2_unit = Soldier()

print(army1_unit)
print(army2_unit)

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

print(army1_unit)
print(army2_unit)