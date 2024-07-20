import numpy as np
from collections import defaultdict
import seaborn as sns
import matplotlib.pyplot as plt

TRIALS = 100_000
FLIPS = [10, 100, 300]
SUCCESS_RATES = [0.05, 0.1, 0.25, 0.3, 0.5, 0.7, 0.9, 0.95]

results = defaultdict(lambda: defaultdict(list))
for success_rate in SUCCESS_RATES:
    for num_flips in FLIPS:
        for _ in range(TRIALS):
            flips = np.random.rand(num_flips)
            flips = flips < success_rate
            streak = 1
            longest_winning_streak = 1 if flips[0] else 0
            longest_losing_streak = 1 if not flips[0] else 0
            for i, flip in enumerate(flips[1:], 1):
                if flip == flips[i - 1]:
                    streak += 1
                else:
                    streak = 1
                if flip:
                    longest_winning_streak = max(longest_winning_streak, streak)
                else:
                    longest_losing_streak = max(longest_losing_streak, streak)

            ratio = longest_winning_streak / max(longest_losing_streak, 1)
            results[success_rate][num_flips].append(ratio)


fig, axs = plt.subplots(
    nrows=len(SUCCESS_RATES),
    ncols=len(FLIPS),
    figsize=(len(FLIPS) * 6, len(SUCCESS_RATES) * 6),
)
for i, (success_rate, ratios) in enumerate(results.items()):
    for j, flips in enumerate(FLIPS):
        mean = np.mean(ratios[flips])
        hist = sns.histplot(
            ratios[flips], kde=True, ax=axs.flatten()[i * len(FLIPS) + j], bins=30
        )
        hist.set_title(f"{flips=}, {success_rate=}, {mean=:0.5f}")
        hist.set_xlabel("Ratio")
        hist.set_ylabel("Frequency")
fig.savefig("out.png")
