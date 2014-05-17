import prisoner

x = prisoner.Dilemma()

def init_test(func):
    for i in range(100):
        x.compute_score(func, x.random_move())

def efficiency_test(func):
    y = prisoner.Dilemma()
    for i in range(100):
        x.compute_score(func, x.random_move())
        y.compute_score(func, x.random_move())

def payoff_test(func):
    for i in range(1000):
        x.compute_score(func, x.random_move())
    print (1.0*x.human_payoff/(x.human_payoff+x.computer_payoff))

def display_prob():
    print x.prob_c
    print x.prob_d
    print x.prob_c_given_d

if __name__ == '__main__':
    init_test(x.tit_for_tat())