if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()
    y = prisoner.Dilemma()
    test_list = [0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0]

    for i in range(1000):
        print x.prob_c
        print x.prob_d
        print x.prob_c_over_d
        y.compute(y.tit_for_tat(), x.random_move())
        x.compute(x.bayesian_move(), x.random_move())