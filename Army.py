from Fighter import *
from Stack import Stack

class Army():
    def __init__(self, player_name, n_soldiers, n_archers, n_cavalry):
        if (n_soldiers < 0) or (n_archers < 0) or (n_cavalry < 0):
            raise ValueError("Numbers of each unit must be ≥ 0")

        self.player = player_name
        self.fighter_stack = Stack(20)

        for s in range(n_cavalry):
            self.fighter_stack.push(Cavalry())
        for a in range(n_archers):
            self.fighter_stack.push(Archer())
        for c in range(n_cavalry):
            self.fighter_stack.push(Soldier())

    def __lt__(self, other):
        return len(self.fighter_stack) < other

    def __gt__(self, other):
        return len(self.fighter_stack) > other

    def __eq__(self, other):
        return len(self.fighter_stack) == other

    def next_fighter(self):
        return self.fighter_stack.pop()