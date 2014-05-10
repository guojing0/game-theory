if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()
    y = prisoner.Dilemma()
    z = prisoner.Dilemma()

    lst = [0, 1, 1, 0, 0, 1, 1, 1, 0, 0]

    for i in xrange(100):
        y.compute(y.win_stay_lose_switch(), x.random_move())
        z.compute(z.bayesian_move(2), x.random_move())