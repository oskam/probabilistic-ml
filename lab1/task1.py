import random

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots()


STOP = 10

ax.set_ylim((0, 1))
ax.set_xlim((-0.4, STOP-0.4))

occurences = [0 for _ in range(0, STOP)]
frequencies = [0.0 for _ in range(0, STOP)]

pos = np.arange(STOP)
width = 0.8     # gives histogram aspect to the bar diagram
ax.set_xticks(pos)
ax.set_xticklabels([str(n) if n % 5 == 0 else '' for n in range(0, STOP)])

rects = plt.bar(pos, frequencies, width, color='r')


def randoms():
    while True:
        yield np.random.randint(0, STOP)


def animate(arg, rects):
    frequencies = arg
    for rect, f in zip(rects, frequencies):
        rect.set_height(f)


def step():
    for i in randoms():
        occurences[i] += 1
        total = sum(occurences)
        for j in range(0, STOP):
            frequencies[j] = occurences[j] / total
        yield frequencies


# call the animator. blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, step,
                               repeat=False, interval=100, fargs=(rects,))
plt.show()
