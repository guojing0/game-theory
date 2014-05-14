if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()

    for i in range(100):
        x.compute_score(x.bayesian_move(2), x.random_move())