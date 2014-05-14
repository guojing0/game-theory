#!/usr/bin/env python

"""
The program is to simulate the prisoner's dilemma:

Cooperation move is 0 and defection move is 1.

random_move() is for computer_choice, but you can choose 0 or 1 yourself.

tit_for_tat(), win_stay_lose_switch() and bayesian_move() are different strategies for human_choice,
and you can choose 0 or 1 yourself for human_choice as well.

After running some tests, I believe 2 is one of the best parameters for bayesian_move() function.
"""

__all__ = [
    'Dilemma', 'display_info',
    'compute_score', 'random_move',
    'tit_for_tat', 'win_stay_lose_switch',
    'bayesian_move', 'naive_bayesian_move'
]

import random

class Dilemma:

    def __init__(self):
        self.rounds = 0
        self.human_payoff = 0
        self.computer_payoff = 0
        self.original_move = 0 # The move before previous_move
        self.previous_move = 0

        # These are for bayesian_move function
        self.history = []
        self.prob_c = 0.5
        self.prob_d = 0.5
        self.prob_c_over_d = 0.5

    def display_info(self, choice):
        print 'Rounds: %d' % self.rounds
        print 'Human payoff: %d' % self.human_payoff
        print 'Computer payoff: %d' % self.computer_payoff
        print 'Computer choice: %d' % choice

    def compute_score(self, human_choice, computer_choice, display_info=True):
        """ If you play with the computer, and then computer_choice should be random_move(). """
        self.rounds += 1
        self.history.append(computer_choice)
        self.original_move = self.previous_move
        self.previous_move = computer_choice

        if (human_choice == computer_choice == 0):
            self.human_payoff += 3
            self.computer_payoff += 3
        elif (human_choice == computer_choice == 1):
            self.human_payoff += 1
            self.computer_payoff += 1
        elif (human_choice == 0 and computer_choice == 1):
            self.computer_payoff += 5
        elif (human_choice == 1 and computer_choice == 0):
            self.human_payoff += 5

        if (display_info == True):
            Dilemma.display_info(self, computer_choice)

    def random_move(self):
        return random.randint(0, 1)

    def tit_for_tat(self):
        return self.previous_move

    def win_stay_lose_switch(self):
        if (self.original_move == self.previous_move):
            self.original_move = 0
        elif (self.original_move != self.previous_move):
            self.original_move = 1
        return self.original_move

    def bayesian_move(self, set_range=None): # Zero should not be assigned to set_range.
        if (set_range == None and self.history == []):
            self.history.extend([0, 1]) # Avoids ZeroDivisionError and self.history == []
        elif (set_range == None):
            self.prob_c = 1.0 * self.history.count(0) / self.rounds
            self.prob_d = 1.0 * self.history.count(1) / self.rounds

        if (set_range != None and len(self.history) < set_range):
            return self.previous_move
        elif (set_range != None):
            self.prob_c = 1.0 * self.history[-set_range:].count(0) / len(self.history[-set_range:])
            self.prob_d = 1.0 * self.history[-set_range:].count(1) / len(self.history[-set_range:])

        if (self.prob_d == 0):
            return 1

        self.prob_c_over_d = 0.5 * self.prob_c / self.prob_d
        if (self.prob_c_over_d >= 0.5):
            return 0
        else:
            return 1

    def naive_bayesian_move(self): # WIP
        pass
