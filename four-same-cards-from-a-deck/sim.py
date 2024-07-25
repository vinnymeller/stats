import random
from collections import defaultdict

# make the deck
CARDS = [
    '2', '2', '2', '2',
    '3', '3', '3', '3',
    '4', '4', '4', '4',
    '5', '5', '5', '5',
    '6', '6', '6', '6',
    '7', '7', '7', '7',
    '8', '8', '8', '8',
    '9', '9', '9', '9',
    '10', '10', '10', '10',
    'J', 'J', 'J', 'J',
    'Q', 'Q', 'Q', 'Q',
    'K', 'K', 'K', 'K',
    'A', 'A', 'A', 'A',
    'Joker', 'Joker'
]
assert len(CARDS) == 54, "I messed up the deck"
assert len(set(CARDS)) == 14, "I messed up the deck"

PLAYERS = 4

TRIALS = 20_000_000

player_one_fourteen_cards = 0
player_one_thirteen_cards = 0
player_one_win_with_fourteen = 0
player_one_win_with_thirteen = 0
anyone_won = 0

for _ in range(TRIALS):

    # shuffle the deck
    random.shuffle(CARDS)

    # give each player an empty collection of cards
    player_hands = [defaultdict(int) for _ in range(PLAYERS)]

    # loop through the shuffled deck of cards
    for i, card in enumerate(CARDS):
        # keep count of the type of card each player has
        player_hands[i % PLAYERS][card] += 1

    # OP is player one, arbitrarily
    ops_deck = random.choice(player_hands)

    op_won = False
    if sum(ops_deck.values()) == 13:
        player_one_thirteen_cards += 1
        if max(ops_deck.values()) == 4:
            player_one_win_with_thirteen += 1
            op_won = True
    else: # must be 14
        player_one_fourteen_cards += 1
        if max(ops_deck.values()) == 4:
            player_one_win_with_fourteen += 1
            op_won = True


    # we don't have to look at all decks if OP won already
    if op_won:
        anyone_won += 1
    else:
        if max([max(hand.values()) for hand in player_hands]) == 4:
            anyone_won += 1

print(f"""
Total trials: {TRIALS}

OP (Player 1) had 14 cards {player_one_fourteen_cards} times ({(player_one_fourteen_cards / TRIALS) * 100:.3f}%)
When OP had 14 cards, OP won {player_one_win_with_fourteen} times ({(player_one_win_with_fourteen / player_one_fourteen_cards) * 100:.3f}%)

OP had 13 cards {player_one_thirteen_cards} times ({(player_one_thirteen_cards / TRIALS) * 100:.3f}%)
When OP had 13 cards, OP won {player_one_win_with_thirteen} times ({(player_one_win_with_thirteen / player_one_thirteen_cards) * 100:.3f}%)

Anyone won {anyone_won} times ({(anyone_won / TRIALS) * 100:.3f}%)
""")

