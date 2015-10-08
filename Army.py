from Fighter import *
from Stack import Stack

class Army():
    def __init__(self, player_name, n_soldiers, n_archers, n_cavalry):
        if (n_soldiers < 0) or (n_archers < 0) or (n_cavalry < 0):
            raise ValueError("Numbers of each unit must be ≥ 0")

        self.player = player_name
        self.soldier_stack = Stack(20)

        for s in range(n_cavalry):
            self.soldier_stack.push(Cavalry())
        for a in range(n_archers):
            self.soldier_stack.push(Archer())
        for c in range(n_cavalry):
            self.soldier_stack.push(Soldier())
