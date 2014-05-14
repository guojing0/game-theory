if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()

    for i in range(50):
        x.compute_score(x.bayesian_move(), x.random_move(), False)
        print 'Cooperation %.3f' % x.prob_c
        print 'Defection %.3f' % x.prob_d
        print 'P(C|D): %.3f' % x.prob_c_over_d

    print '%.3f' % (x.human_payoff/((x.human_payoff+x.computer_payoff) * 1.0))