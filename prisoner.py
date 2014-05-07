#!/usr/bin/python
import random

# The program is to simulate the prisoner's dilemma
# Cooperation move is 0 and defection move is 1
# tit_for_tat() and win_stay_lose_switch() are two different strategies for human_choice
# Of course you can choose 0 or 1 yourself for human_choice
# random_move() is for computer_choice

class Dilemma:

    def __init__(self):
        self.rounds = 0
        self.human_payoff = 0
        self.computer_payoff = 0
        self.original_move = 1 # The move before previous_move
        self.previous_move = 0

    def display_message(self, choice):
        print 'Rounds: %d' % self.rounds
        print 'Human payoff: %d' % self.human_payoff
        print 'Computer payoff: %d' % self.computer_payoff
        print 'Computer choice: %d' % choice

    def compute(self, human_choice, computer_choice):
        """ If you play with the computer, and then computer_choice should be random_move(). """
        self.original_move = self.previous_move
        self.previous_move = computer_choice
        self.rounds += 1
        
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
