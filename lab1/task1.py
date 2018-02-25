import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation

STOP = 10

occurrences = [0 for _ in range(0, STOP)]
frequencies = [0.0 for _ in range(0, STOP)]

fig, ax = plt.subplots()

ax.set_xlabel('Range of the numbers in the stream')
ax.set_ylim((0, 1))
ax.set_xlim((-0.4, STOP-0.4))

pos = np.arange(STOP)
width = 0.8
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
        occurrences[i] += 1
        total = sum(occurrences)
        for j in range(0, STOP):
            frequencies[j] = occurrences[j] / total
        yield frequencies


anim = animation.FuncAnimation(fig, animate, step,
                               repeat=False, interval=100, fargs=(rects,))
plt.show()
