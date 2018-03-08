import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation

K = 20 # number of samples
SCALE = 1.0

means = np.zeros(K)

fig, ax = plt.subplots()

ax.set_xlabel('Range of the numbers in the stream')
ax.set_ylim((0, 2.0))

pos = np.arange(K)
width = 0.8

rects = plt.bar(pos, means, width, color='b')

def samples(N):
    for _ in range(K):
        yield np.random.exponential(scale=SCALE, size=N)


def animate(arg, rects):
    for rect, f in zip(rects, arg):
        rect.set_height(f)


def inf_range():
    n = 0
    while True:
        n += 1
        yield n

def step():
    for n in inf_range():
        for i, sample in enumerate(samples(n)):
            means[i] = np.mean(sample)
        yield means

anim = animation.FuncAnimation(fig, animate, step,
                               repeat=False, interval=10, fargs=(rects,))
plt.show()

