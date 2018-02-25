import matplotlib.pyplot as plt

# A - ill
# B - positive test result

# const:
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

fig, ax = plt.subplots()
fig.canvas.draw()
ax.plot(xs, ys, '-o', ms=3, lw=2, alpha=0.7, mfc='blue')
ax.set_xlabel('Number of sick people in population')
ax.set_ylabel('Probability that positive test is correct')
labels = [x if x % 10 == 0 else '' for x in range(1, 101)]
plt.xticks(xs, labels)

plt.show()
