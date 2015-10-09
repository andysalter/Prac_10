from Fighter import *
from Stack import Stack


class Army():
    def __init__(self, player_name, n_soldiers, n_archers, n_cavalry):
        """
        Complexity: O(n)
        :param player_name: Name of player
        :param n_soldiers:  The number of soldiers to be created
        :param n_archers:   The number of archers to be created
        :param n_cavalry:   The number of cavalrymen to be created
        """
        if (n_soldiers < 0) or (n_archers < 0) or (n_cavalry < 0):
            raise ValueError("Numbers of each unit must be ≥ 0")

        self.player = player_name
        self.fighter_stack = Stack(20)

        self.n_soldiers = n_soldiers
        self.n_archers = n_archers
        self.n_cavalry = n_cavalry

        for s in range(self.n_cavalry):
            self.fighter_stack.push(Cavalry())
        for a in range(self.n_archers):
            self.fighter_stack.push(Archer())
        for c in range(self.n_cavalry):
            self.fighter_stack.push(Soldier())

    def __lt__(self, other):
        return len(self.fighter_stack) < other

    def __gt__(self, other):
        return len(self.fighter_stack) > other

    def __eq__(self, other):
        return len(self.fighter_stack) == other

    def next_fighter(self):
        return self.fighter_stack.pop()