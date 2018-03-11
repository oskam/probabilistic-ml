import numpy as np
import matplotlib.pyplot as plt
import scipy

from matplotlib import animation

p = 0.5  # probability of success
k = 1000  # number of trials runs
min_n = 0  # number of trials
max_n = 100
step_n = 10


def bernoulli_trials(n, p):
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success


def bernoulli_k_trials_using_binomial(k, n, p):
    res = np.zeros(k, dtype=int)
    for i, _ in enumerate(res):
        res[i] = sum(np.random.binomial(1, p, n))  # array with sum of successes in runs of size n
    return res


# -----plot------
fig, ax = plt.subplots()
ax.set_ylim(bottom=0)
ax.set_xlim((min_n, max_n + 1))
pos = np.arange(max_n + 1)
ax.set_xticks(pos)
ax.set_xticklabels([str(n) if n % 5 == 0 else '' for n in range(0, max_n + 1)])
width = 0.8

rects = plt.bar(pos, np.zeros(max_n + 1), width, color='b', align='center')


def animate(arg, rects):
    ax.set_ylim(bottom=0, top=max(arg), emit=True)
    for rect, f in zip(rects, arg):
        rect.set_height(f)


# def step():
#     for n in range(min_n+step_n, max_n+1, step_n):
#         plt.title(f"n = {n}")
#         results = np.zeros(n)
#         for i in range(n):
#             results[i] = scipy.stats.binom.pmf(i, n, p)
#         yield results


def step():
    for n in range(min_n + step_n, max_n + 1, step_n):
        plt.title(f"n = {n}; k = {k}; p_suc = {p}")
        runs = bernoulli_k_trials_using_binomial(k, n, p)
        sucs = np.zeros(n + 1)
        for r in runs:
            sucs[r] += 1  # index is a number of successes
        res = np.zeros(n + 1)
        for i, _ in enumerate(res):
            res[i] = sucs[i] / k
        yield res


anim = animation.FuncAnimation(fig, animate, step,
                               repeat=False, interval=2000, fargs=(rects,))
plt.show()
