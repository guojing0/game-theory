if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()

    for m in range(1,10):
        for i in range(100):
            x.compute_score(x.bayesian_move(m), x.random_move(), display_info=False)

    print len(x.history)
    print x.history.count(0)
    print x.history.count(1) 