import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

from matplotlib import animation


p = 0.7 # probability of success
# n = 100 # number of trials
num_of_successes = 0

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
    n_success = 0
    for _ in range(n):
        x = np.random.binomial(1, p)
        if x == 1:
            n_success += 1
    return n_success

# -----plot------
fig, ax = plt.subplots()
pos = np.arange(2)
width = 0.8
results = np.zeros(2)

rects = plt.bar(pos, results, width, color='b')

def animate(arg, rects):
    for rect, f in zip(rects, arg):
        rect.set_height(f)


def inf_range():
    n = 0
    while True:
        n += 1
        yield n


def step():
    num_of_successes = 0
    for n in inf_range():
        k = np.random.binomial(1, p)
        if x == 1:
            num_of_successes += 1
        pmf = bernoulli.pmf(k, p)
    yield results

anim = animation.FuncAnimation(fig, animate, step,
                               repeat=False, interval=10, fargs=(rects,))
plt.show()