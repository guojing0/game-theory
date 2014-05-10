if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()
    y = prisoner.Dilemma()

    for f in xrange(11):
        for i in xrange(2000):
            x.compute_score(x.tit_for_tat(), x.random_move(), display=False)
            y.compute_score(y.bayesian_move(f), x.random_move(), display=False)

        sum_of_x = x.human_payoff + x.computer_payoff
        temp_var = 1.0 * (sum_of_x - y.human_payoff - y.computer_payoff) / sum_of_x
        ratio = 1.0 * y.human_payoff / (y.human_payoff + y.computer_payoff)

        if (ratio >= 0.5 or temp_var < 0):
            print '%d ratio: %f differ: %f' % (f, ratio, temp_var)

        x.__init__()
        y.__init__()