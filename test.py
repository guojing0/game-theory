if __name__ == '__main__':
    import prisoner

    x = prisoner.Dilemma()
    y = prisoner.Dilemma()

    num_x = 0
    num_y = 0

    for i in range(5000):
        x.compute_score(x.win_stay_lose_switch(), x.random_move(), display_info=False)
        y.compute_score(y.bayesian_move(2), x.random_move(), display_info=False)

        if (x.human_payoff > x.computer_payoff):
            num_x += 1
        elif (y.human_payoff > y.computer_payoff):
            num_y += 1

    print 'X %.3f' % (1.0 * num_x / 5000)
    print 'Y %.3f' % (1.0 * num_y / 5000)
