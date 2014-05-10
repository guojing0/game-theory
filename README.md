### Game theory

> Programs to test game theory

##### If you find it fun and helpful, you can help me via [`Gittip`](https://www.gittip.com/guojing0/) or [`Paypal`](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Y6RGUQ552NHKS).

#### Programs

* prisoner.py - Simulate a prisoner's dilemma.
* test.py - Some simple tests I run.

#### Examples

```
>>> import prisoner
>>> example = prisoner.Dilemma()
>>> example.compute_score(example.tit_for_tat(), example.random_move())
Rounds: 1
Human payoff: 3
Computer payoff: 3
Computer choice: 0
>>> example.compute_score(example.win_stay_lose_switch(), example.random_move()) 
Rounds: 2
Human payoff: 3
Computer payoff: 8
Computer choice: 1
>>> example.compute_score(example.bayesian_move(), example.random_move()) 
Rounds: 3
Human payoff: 3
Computer payoff: 13
Computer choice: 1
>>> example.compute_score(example.bayesian_move(2), example.random_move())
Rounds: 4
Human payoff: 8
Computer payoff: 13
Computer choice: 0
```

#### Contributors

* [Jing Guo](http://guoj.org/)
* You (Pull requests and contribute!)

#### License

MIT. Copyright (c) [Jing Guo](http://guoj.org/)