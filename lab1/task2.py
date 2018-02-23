# import random
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib import animation


STOP = 10
occurences = [[0 for _ in range(0, STOP)] for _ in range(0, STOP)]
frequencies = [[0 for _ in range(0, STOP)] for _ in range(0, STOP)]


def randoms():
    while True:
        yield np.random.randint(0, STOP)
        # yield random.randint(0, STOP-1)


fig = plt.figure()


def animate(arg):
    plt.clf()
    frequencies = arg
    data = frequencies
    sns.heatmap(data, robust=True, square=True, cmap="gist_heat").invert_yaxis()


def step():
    for i in randoms():
        try:
            occurences[prev][i] += 1
        except UnboundLocalError:
            pass
        total = sum(map(sum, occurences))
        for x, _ in enumerate(occurences):
            for y, o in enumerate(occurences[x]):
                try:
                    frequencies[x][y] = o / total
                except ZeroDivisionError:
                    frequencies[x][y] = 0
        prev = i
        yield frequencies


anim = animation.FuncAnimation(fig, animate, step, interval=5, repeat=False)
plt.show()
