import numpy as np
import scipy.stats
from scipy.special import factorial

probs = [.02, .05, .15, .1, .15, .1, .3, .07, .06]

# 1 (Poisson binomial distribution)
# (1-p1)(1-p2)...(1-p9)
prob = [1 - x for x in probs]
result = np.prod(np.array(prob))
print(result)

# 2
# x = 9 # liczba kierunkow
# num_of_successes = 0 # na ile się dostał
#
# ns = np.zeros(x, dtype=int)
# ns[num_of_successes] = 1
# print(ns)
#
# ns_fact = np.prod([factorial(n) for n in ns])
#
# probs_to_ns = np.prod([(prob ** n) for prob, n in zip(probs, ns)])
#
# total_prob = (1 / ns_fact) * probs_to_ns
#
# print(total_prob)
