if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()

    for i in range(50):
        x.compute_score(x.bayesian_move(), x.random_move())