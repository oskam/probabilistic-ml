import numpy as np
import scipy.stats

# binomial distribution
# pmf(x) = (n choose x) * p^x * (1-p)^(n-x)
# where:
# n - number of trails
# p - probability of success
# x - number of successes

x = 0
p = 0.1
n = 9

# 1 numpy
print(sum(np.random.binomial(9, 0.1, 10000) == 0) / 10000)

# 2 scipy
print(scipy.stats.binom.pmf(x, n, p))


# 3 me
def binomial_coefficient(n, x):
    if x == 0:
        return 1
    if n == 0:
        return 0
    res = binomial_coefficient(n - 1, x) + binomial_coefficient(n - 1, x - 1)
    return res


def binomial_distribution(n, p, x):
    return binomial_coefficient(n, x) * (p ** x) * ((1 - p) ** (n - x))


print(binomial_distribution(n, p, x))
