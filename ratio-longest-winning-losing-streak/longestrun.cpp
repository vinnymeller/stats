#include <gmpxx.h>
#include <iomanip>
#include <iostream>
#include <vector>

using namespace std;

mpf_class biased_coin_recursion(int x, int n, double floatp) {
  double floatq = 1 - floatp;

  mpf_class p(floatp, 500);
  mpf_class q(floatq, 500);
  vector<vector<mpz_class>> coefs(n + 1, vector<mpz_class>(n + 1, 0));

  for (int i = 0; i <= n; ++i) {
    for (int j = 0; j <= i; ++j) {
      if (j <= x) {
        mpz_bin_uiui(coefs[i][j].get_mpz_t(), i, j);
      } else {
        mpz_class summation(0);
        for (int k = 0; k <= x; ++k) {
          if (i - k - 1 >= 0 && j - k >= 0) {
            summation += coefs[i - k - 1][j - k];
          }
        }
        coefs[i][j] = summation;
      }
    }
  }

  mpf_class prob(0, 500);
  for (int i = 0; i <= n; ++i) {
    mpf_class term(0, 500);
    mpf_class first(0, 500);
    mpf_class second(0, 500);
    mpf_pow_ui(first.get_mpf_t(), p.get_mpf_t(), i);
    mpf_pow_ui(second.get_mpf_t(), q.get_mpf_t(), (n - i));
    mpf_set_z(term.get_mpf_t(), coefs[n][i].get_mpz_t());
    term *= first;
    term *= second;
    prob += term;
  }
  return prob;
}

int main() {
  vector<int> FLIPS = {10, 100, 300};
  vector<double> SUCCESS_RATES = {0.05, 0.1, 0.25, 0.3, 0.5, 0.7, 0.9, 0.95};

  for (int flips : FLIPS) {
    for (double success_rate : SUCCESS_RATES) {
      double fail_rate = 1 - success_rate;
      vector<mpf_class> win_streak_cum_probs(flips + 1);
      vector<mpf_class> loss_streak_cum_probs(flips + 1);

      for (int max_streak = 0; max_streak <= flips; ++max_streak) {
        win_streak_cum_probs[max_streak] =
            biased_coin_recursion(max_streak, flips, success_rate);
        loss_streak_cum_probs[max_streak] =
            biased_coin_recursion(max_streak, flips, fail_rate);
      }

      // Calculate exact probabilities
      vector<mpf_class> win_streak_exact_probs(flips + 1);
      vector<mpf_class> loss_streak_exact_probs(flips + 1);

      win_streak_exact_probs[0] = win_streak_cum_probs[0];
      loss_streak_exact_probs[0] = loss_streak_cum_probs[0];

      for (int i = 1; i <= flips; ++i) {
        win_streak_exact_probs[i] =
            win_streak_cum_probs[i] - win_streak_cum_probs[i - 1];
        loss_streak_exact_probs[i] =
            loss_streak_cum_probs[i] - loss_streak_cum_probs[i - 1];
      }

      // Calculate expected ratio
      mpf_class expected_ratio(0, 500);
      for (int k = 0; k <= flips; ++k) {
        for (int l = 0; l <= flips; ++l) {
          if (l != 0) {
            mpf_class term = win_streak_exact_probs[k] *
                             loss_streak_exact_probs[l] *
                             mpf_class(double(k) / l, 500);
            expected_ratio += term;
          }
        }
      }

      cout << "flips=" << flips << ", success_rate=" << success_rate
           << ", expected_ratio=" << expected_ratio << endl;
    }
  }

  return 0;
}
