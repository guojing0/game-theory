#!/usr/bin/python

__all__ = [
    'Dilemma', 'display_message',
    'compute_score', 'random_move',
    'tit_for_tat', 'win_stay_lose_switch', 'bayesian_move' 
]

import random

# The program is to simulate the prisoner's dilemma
# Cooperation move is 0 and defection move is 1
# tit_for_tat() and win_stay_lose_switch() are two different strategies for human_choice
# Of course you can choose 0 or 1 yourself for human_choice
# random_move() is for computer_choice
# bayesian_move(set_range=None) is a strategy based on Bayes' theorem

class Dilemma:

    def __init__(self):
        self.rounds = 0
        self.human_payoff = 0
        self.computer_payoff = 0
        self.original_move = 0 # The move before previous_move
        self.previous_move = 0

        self.history = [0, 1] # The initial list prevents bayesian_move(set_range=None) from ZeroDivisionError
        self.prob_c = 0.5
        self.prob_d = 0.5
        self.prob_c_over_d = 0.5

    def display_message(self, choice):
        print 'Rounds: %d' % self.rounds
        print 'Human payoff: %d' % self.human_payoff
        print 'Computer payoff: %d' % self.computer_payoff
        print 'Computer choice: %d' % choice

    def compute_score(self, human_choice, computer_choice, display=True):
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

        if (display == True):
            Dilemma.display_message(self, computer_choice)

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

    def bayesian_move(self, set_range=None): # Still needs fixes
        if (set_range == None):
            self.prob_c = 1.0 * self.history.count(0) / len(self.history)
            self.prob_d = 1.0 * self.history.count(1) / len(self.history)
        elif (len(self.history) < set_range):
            return self.previous_move
        else:
            self.prob_c = 1.0 * self.history[-set_range:].count(0) / len(self.history[-set_range:])
            self.prob_d = 1.0 * self.history[-set_range:].count(1) / len(self.history[-set_range:])
            if (self.prob_d == 0):
                return 1

        self.prob_c_over_d = 0.5 * self.prob_c / self.prob_d
        if (self.prob_c_over_d >= 0.5):
            return 0
        else:
            return 1
