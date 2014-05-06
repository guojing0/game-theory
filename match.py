#!/usr/bin/python
import random

class Match:

    def __init__(self):
        self.rounds = 0
        self.correct_num = 0

    def display_message(self, choice):
        print "Rounds: %d" % self.rounds
        print "Score: %d" % self.correct_num
        print "Computer choice: %d" % choice

    def play(self, choice):
        computer_choice = random.randint(0, 1)
        if choice == computer_choice:
            self.rounds += 1
            self.correct_num += 1
            Match.display_message(self, computer_choice)
        else:
            self.rounds += 1
            Match.display_message(self, computer_choice)