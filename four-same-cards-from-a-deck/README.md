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
Trials: 20000000

OP (Player 1) had 14 cards 9997461 times (49.987%)
When OP had 14 cards, OP won 409513 times (4.096%)

OP had 13 cards 10002539 times (50.013%)
When OP had 13 cards, OP won 293080 times (2.930%)

Anyone won 2630807 times (13.154%)
```
