import prisoner

x = prisoner.Dilemma()

def init_test():
    for i in range(100):
        x.compute_score(x.____(), x.random_move())

def efficiency_test():
    y = prisoner.Dilemma()
    for i in range(100):
        x.compute_score(x.____(), x.random_move())
        y.compute_score(y.____(), x.random_move())

def payoff_test():
    for i in range(1000):
        x.compute_score(x.____(), x.random_move())
    print (1.0*x.human_payoff/(x.human_payoff+x.computer_payoff))

if __name__ == '__main__':
    pass