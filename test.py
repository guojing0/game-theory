if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()
    y = prisoner.Dilemma()

    for i in range(2500):
        print x.prob_c
        print x.prob_d
        print x.prob_c_over_d
        y.compute(y.tit_for_tat(), x.random_move())
        x.compute(x.bayesian_move(3), x.random_move())