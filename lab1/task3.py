import random

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# A - ill
# B - positive test

# const:
P_B_if_A = 0.99
P_B_if_not_A = 0.02

xs = [i/5e4 for i in range(1,101)]

def get_y(x):
    p_B = (P_B_if_A * x) + (P_B_if_not_A * (1-x))
    return (P_B_if_A * x) / p_B

ys = [get_y(x) for x in xs]

plt.plot(xs, ys)

plt.show()