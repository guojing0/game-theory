if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()
    y = prisoner.Dilemma()
    x.history = [0, 1]

    hist = [1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1]

    for i in hist:
        print x.prob_c, y.prob_c
        print x.prob_d, y.prob_d
        print x.prob_c_over_d, y.prob_c_over_d
        x.compute(x.bayesian_move(), i)
        y.compute(y.bayesian_move(), i)