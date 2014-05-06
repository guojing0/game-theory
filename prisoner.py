#!/usr/bin/python
import random

class Dilemma: # Prisoner's Dilemma

    def __init__(self):
        self.rounds = 0
        self.human_payoff = 0
        self.computer_payoff = 0

    def display_message(self, choice):
        print "Rounds: %d" % self.rounds
        print "Human payoff: %d" % self.human_payoff
        print "Computer payoff: %d" % self.computer_payoff
        print "Computer choice: %d" % choice

    def start(self, human_choice):
        computer_choice = random.randint(0, 1) # Cooperation is 0 and Defection is 1
        if (human_choice == computer_choice == 0):
            self.rounds += 1
            self.human_payoff += 3
            self.computer_payoff += 3
            Dilemma.display_message(self, computer_choice)
        elif (human_choice == computer_choice == 1):
            self.rounds += 1
            self.human_payoff += 1
            self.computer_payoff += 1
            Dilemma.display_message(self, computer_choice)
        elif (human_choice == 0 and computer_choice == 1):
            self.rounds += 1
            self.computer_payoff += 5
            Dilemma.display_message(self, computer_choice)
        elif (human_choice == 1 and computer_choice == 0):
            self.rounds += 1
            self.human_payoff += 5
            Dilemma.display_message(self, computer_choice)