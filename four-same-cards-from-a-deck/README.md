# four same cards from a deck

Simulation to answer reddit post [here](https://www.reddit.com/r/AskStatistics/comments/1eb6w0y/probability_help_this_has_stumped_all_my_friends/)

tldr, you have a full deck of cards + 2 jokers. you distribute the cards randomly between 4 players

What is the likelihood that you get 4 of the same card (e.g. 4 aces or 4 sevens) in your hand when you have 13 cards? 14 cards?

What is the probability that any of the 4 players wins (has 4 of the same card)?


## Result

This script has no external dependencies.

```bash
python sim.py
```

Result:

```
Total trials: 10000000

OP (Player 1) had 14 cards 5000848 times (50.01%)
When OP had 14 cards, OP won 188986 times (3.78%)

OP had 13 cards 4999152 times (49.99%)
When OP had 13 cards, OP won 135001 times (2.70%)

Anyone won 1220529 times (12.21%)
```
