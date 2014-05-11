if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()
    y = prisoner.Dilemma()

    sum_of_x = 0
    sum_of_y = 0

    y.history = []

    for z in range(20):
        for i in range(2000):
            x.compute_score(x.bayesian_move(2), x.random_move(), display_info=False)
            y.compute_score(y.bayesian_move(2), x.random_move(), display_info=False)

        num_x = x.human_payoff + x.computer_payoff
        num_y = y.human_payoff + y.computer_payoff

        if (num_x > num_y):
            sum_of_x += 1
        else:
            sum_of_y += 1

    print sum_of_x, sum_of_y
