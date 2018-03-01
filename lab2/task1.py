import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

NUM_OF_PLOTS = 3
TRIES = int(1e2)
STD_DEV = [0.5, 1, 2]


def plot(num):
    legend_data = []
    f, axes = plt.subplots()
    for i in range(num):
        data = [np.random.normal(scale=STD_DEV[i]) for _ in range(TRIES)]
        r, g, b = np.random.sample(3)
        mean = np.mean(data)
        legend_data.append(str(i+1) + ".  mean: " + str(round(mean, 2)) + "  variance: " + str((STD_DEV[i])*2))
        sns.distplot(data, kde=True, hist=False, color=(r,g,b))
        axes.axvline(mean, color=(r,g,b), linestyle='--')
    plt.legend(legend_data, bbox_to_anchor=(1.1, 1))
    plt.show()


plot(NUM_OF_PLOTS)
