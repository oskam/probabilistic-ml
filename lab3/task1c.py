import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import bernoulli

from matplotlib import animation


# p = [0.5, 0.3, 0.2]  # probability of success
p = 0.5  # probability of success
min_n = 0  # number of trials
max_n = 100
step_n = 10


def bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
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


def bernoulli_trials_using_binomial(n, p):
    x = np.random.binomial(1, p, n)
    return x


# -----plot------
fig, ax = plt.subplots()
ax.set_ylim(bottom=0)
ax.set_xlim((0, max_n))
pos = np.arange(max_n)
ax.set_xticks(pos)
ax.set_xticklabels([str(n) if n % 5 == 0 else '' for n in range(0, max_n)])
width = 0.8

results = np.zeros(max_n)

rects = plt.bar(pos, results, width, color='b', align='center')


def animate(arg, rects):
    ax.set_ylim(bottom=0, top=max(arg), emit=True)
    for rect, f in zip(rects, arg):
        rect.set_height(f)


def step():
    for n in range(min_n+step_n, max_n+1, step_n):
        plt.title(f"n = {n}")
        results = np.zeros(n)
        # combs = [[a, b, c] for a in range(n) for b in range(n) for c in range(n) if a+b+c == n]
        for i in range(n):
            results[i] = scipy.stats.multinomial.pmf([i, n-i], n, [p, 1.0-p])
        yield results


anim = animation.FuncAnimation(fig, animate, step,
                               repeat=False, interval=2000, fargs=(rects,))
plt.show()
