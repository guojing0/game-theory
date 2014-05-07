### Game theory

> Programs to test game theory

#### Programs

* match.py - Match your choice to computer's choice.

* prisoner.py - Simulate a prisoner's dilemma.

#### Examples

```
>>> import prisoner
>>> example = prisoner.Dilemma()
>>> example.compute(example.tit_for_tat(), example.random_move())
Rounds: 1
Human payoff: 3
Computer payoff: 3
Computer choice: 0
>>> example.compute(example.tit_for_tat(), example.random_move())
Rounds: 2
Human payoff: 3
Computer payoff: 8
Computer choice: 1
>>> example.compute(example.win_stay_lose_switch(), example.random_move())
Rounds: 3
Human payoff: 4
Computer payoff: 9
Computer choice: 1
```

#### Contributors

* [Jing Guo](http://guoj.org/)
* You (Pull requests and contribute!)

#### License

MIT. Copyright (c) [Jing Guo](http://guoj.org/)