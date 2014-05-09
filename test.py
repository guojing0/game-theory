if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()

    for i in range(10):
        print x.prob_c
        print x.prob_d
        print x.prob_c_over_d
        x.compute(x.bayesian_move(), x.random_move())
    print x.history