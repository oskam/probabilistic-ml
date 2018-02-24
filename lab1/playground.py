# negative test if im not ill?

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# not_A - healthy
# not B - negative test result

# const:
PROB_NOT_B_IF_NOT_A = 0.98  # prob that the test will yield a positive result [B] if the disease is present [A]
PROB_NOT_B_IF_A = 0.01  # prob that the test will yield a positive result [B] if the disease is not  present [~A]

xs = [i / 5e4 for i in range(1, 101)]


def get__not_y(x):
    # count prob of a positive test result [B], irrespective of
    # whether the disease is present [A] or not present [~A]
    # then return prob that a positive test result will be a true positive
    prob_not_b = (PROB_NOT_B_IF_A * (1-x)) + (PROB_NOT_B_IF_NOT_A *x)
    return (PROB_NOT_B_IF_NOT_A * (1-x))/ prob_not_b


PROB_B_IF_A = 0.99  # prob that the test will yield a positive result [B] if the disease is present [A]
PROB_B_IF_NOT_A = 0.02  # prob that the test will yield a positive result [B] if the disease is not  present [~A]

xs = [i / 5e4 for i in range(1, 101)]


def get_y(x):
    # count prob of a positive test result [B], irrespective of
    # whether the disease is present [A] or not present [~A]
    # then return prob that a positive test result will be a true positive
    prob_b = (PROB_B_IF_A * x) + (PROB_B_IF_NOT_A * (1 - x))
    return (PROB_B_IF_A * x) / prob_b


ys = [get_y(x) for x in xs]

# plt.plot(xs, ys)
fig, ax = plt.subplots()
ax.plot(xs, ys,  '-o', ms=3, lw=2, alpha=0.7, mfc='blue')
ys = [get_y(x) for x in xs]
not_ys =[get__not_y(x) for x in xs]

# plt.plot(xs, ys)
fig, ax = plt.subplots()
ax.plot(xs, ys, 'r', xs, not_ys, 'b')
ax.grid()


# labels = [str(x) if x % 10 == 0 else '' for x in xs]
# ax.set_xticks(xs, labels)
# ax.set_xticklabels([str(x) if x % 5 == 0 else '' for x in xs])


plt.show()