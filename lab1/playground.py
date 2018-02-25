# negative test if i'm not ill?

import matplotlib.pyplot as plt

# not_A - healthy
# not B - negative test result

# const:
PROB_NOT_B_IF_NOT_A = 0.98
PROB_NOT_B_IF_A = 0.01
PROB_B_IF_A = 0.99
PROB_B_IF_NOT_A = 0.02

xs = [i / 5e4 for i in range(1, 101)]


def get__not_y(x):
    prob_not_b = (PROB_NOT_B_IF_A * (1-x)) + (PROB_NOT_B_IF_NOT_A *x)
    return (PROB_NOT_B_IF_NOT_A * (1-x))/ prob_not_b


def get_y(x):
    prob_b = (PROB_B_IF_A * x) + (PROB_B_IF_NOT_A * (1 - x))
    return (PROB_B_IF_A * x) / prob_b


ys = [get_y(x) for x in xs]

fig, ax = plt.subplots()
not_ys = [get__not_y(x) for x in xs]
ax.plot(xs, ys, 'r', xs, not_ys, 'b')
labels = [x if x % 10 == 0 else '' for x in range(1, 101)]
plt.xticks(xs, labels)
ax.grid()
plt.show()
