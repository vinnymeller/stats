import random

# simulate bertrand's box paradox
# there are 3 boxes, the left box has 2 gold coins, the middle box has 1 gold 1 silver, and the right box 2 silver coins
# you pick a random box and draw a coin. it's gold. you draw the second coin from the box you chose. what's the probability that the next coin is gold?

TRIALS = 10_000_000

# 1 represents a gold coin, 0 represents a silver coin
BOXES = [ [1, 1], [1, 0], [0, 0] ]

# keep track of how many times the first coin is gold or silver, and how many times the second coin is gold or silver
first_coin_silver = 0
first_coin_gold = 0
second_coin_gold = 0
second_coin_silver = 0

for _ in range(TRIALS):

    # choose a random box
    box = random.choice(BOXES)

    # randomly select index 0 or 1 to choose the coin
    first_coin_index = random.randint(0, 1)
    first_coin = box[first_coin_index]
    
    # if we picked a silver coin, we go to the next trial
    if first_coin == 0:
        first_coin_silver += 1
        continue

    first_coin_gold += 1

    second_coin = box[1 - first_coin_index] # if our first index was 0, we choose index 1, & vice versa

    if second_coin == 1:
        second_coin_gold += 1
    else:
        second_coin_silver += 1
    
print(f"""
Total trials: {TRIALS}
First coin was silver {(first_coin_silver / TRIALS) * 100:.2f}% of the time
First coin was gold {(first_coin_gold / TRIALS) * 100:.2f}% of the time

When the first coin was gold, the second coin was:

Gold {(second_coin_gold / first_coin_gold) * 100:.2f}% of the time
Silver {(second_coin_silver / first_coin_gold) * 100:.2f}% of the time
""")
