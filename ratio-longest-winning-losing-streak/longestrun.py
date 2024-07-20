from decimal import Decimal, getcontext
from scipy.special import comb

FLIPS = [10, 100]
SUCCESS_RATES = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]


def biased_coin_recursion(x, n, p):
    q = 1 - p
    coefs = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(i + 1):
            if j <= x:
                coefs[i][j] = comb(i, j, exact=True)
            else:
                sumation = 0
                for k in range(x + 1):
                    sumation = sumation + coefs[i - k - 1][j - k]
                coefs[i][j] = sumation
    prob = Decimal(0)
    getcontext().prec = 20
    for i in range(len(coefs)):
        num1 = Decimal(p) ** Decimal(i) * Decimal(q) ** Decimal(n - i)
        prob = prob + (coefs[len(coefs) - 1][i] * num1)
    return prob


for j, flips in enumerate(FLIPS):
    for i, success_rate in enumerate(SUCCESS_RATES):
        fail_rate = 1 - success_rate
        win_streak_cum_probs = []
        loss_streak_cum_probs = []
        for max_streak in range(0, flips + 1):
            win_streak_prob = biased_coin_recursion(max_streak, flips, success_rate)
            loss_streak_prob = biased_coin_recursion(max_streak, flips, fail_rate)
            win_streak_cum_probs.append(win_streak_prob)
            loss_streak_cum_probs.append(loss_streak_prob)

        # win_streak_cum_probs and loss_streak_cum_probs represent the probability at each index i that the longest streak for the respective
        # outcome does not exceed i. From these, we must extract the probability for each i, that the longest streak for the respective outcome
        # is exactly i. This is done by subtracting the cumulative probability at i-1 from the cumulative probability at i.
        win_streak_exact_probs = [win_streak_cum_probs[0]]
        for i in range(1, len(win_streak_cum_probs)):
            win_streak_exact_probs.append(win_streak_cum_probs[i] - win_streak_cum_probs[i - 1])

        loss_streak_exact_probs = [loss_streak_cum_probs[0]]
        for i in range(1, len(loss_streak_cum_probs)):
            loss_streak_exact_probs.append(loss_streak_cum_probs[i] - loss_streak_cum_probs[i - 1])

        expected_ratio = 0
        for k, win_streak_prob in enumerate(win_streak_exact_probs):
            for l, loss_streak_prob in enumerate(loss_streak_exact_probs):
                expected_ratio += (
                    win_streak_prob * loss_streak_prob * Decimal(k / max(l, 1))
                )

        print(f"{flips=}, {success_rate=}, {expected_ratio=}")
