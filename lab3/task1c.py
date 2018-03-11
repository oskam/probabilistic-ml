import numpy as np
import matplotlib.pyplot as plt
import scipy


from matplotlib import animation


p = 0.5  # probability of success
k = int(1e5)
min_n = 0  # number of trials
max_n = 100
step_n = 10


def k_trials_using_multinomial(k, n, p):
    res = np.zeros(k, dtype=int)
    for i, _ in enumerate(res):
        res[i], _ = np.random.multinomial(n, [p, 1.0-p])
    return res


# -----plot------
fig, ax = plt.subplots()
ax.set_ylim(bottom=0)
ax.set_xlim((min_n, max_n+1))
pos = np.arange(max_n+1)
ax.set_xticks(pos)
ax.set_xticklabels([str(n) if n % 5 == 0 else '' for n in range(0, max_n+1)])
width = 0.8

rects = plt.bar(pos, np.zeros(max_n+1), width, color='b', align='center')


def animate(arg, rects):
    ax.set_ylim(bottom=0, top=max(arg), emit=True)
    for rect, f in zip(rects, arg):
        rect.set_height(f)


# def step():
#     for n in range(min_n+step_n, max_n+1, step_n):
#         plt.title(f"n = {n}")
#         results = np.zeros(n)
#         for i in range(n):
#             results[i] = scipy.stats.multinomial.pmf([i, n-i], n, [p, 1.0-p])
#         yield results

def step():
    for n in range(min_n+step_n, max_n+1, step_n):
        plt.title(f"n = {n}; k = {k}; p_suc = {p}")
        runs = k_trials_using_multinomial(k, n, p)
        sucs = np.zeros(n+1)
        for r in runs:
            sucs[r] += 1
        res = np.zeros(n+1)
        for i, _ in enumerate(res):
            res[i] = sucs[i] / k
        yield res


anim = animation.FuncAnimation(fig, animate, step,
                               repeat=False, interval=2000, fargs=(rects,))
plt.show()
