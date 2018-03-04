import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# probability density for the Gaussian dist. is:
# p(x) = 1 / sqr(2*π*σ^2) * e^(-(x-μ)^2 / (2σ^2))

NUM_OF_PLOTS = 3
SAMPLES = int(1e5)
STD_DEV = [1, 2, 1, 3]  # σ sigma
LOCATION = [0, 5, 8, 15]  # μ mi
SHOW_COMPONENTS = False


def plot():
    legend_data = []
    data_set = []
    f, axes = plt.subplots()
    plt.title("number of: plots=" + str(NUM_OF_PLOTS) + "   samples=" + str(SAMPLES))

    for i in range(NUM_OF_PLOTS):
        data = [np.random.normal(scale=STD_DEV[i], loc=LOCATION[i]) for _ in range(SAMPLES)]
        data_set.append(data)
        if SHOW_COMPONENTS:
            r, g, b = np.random.sample(3)
            sns.distplot(data, kde=True, hist=False, color=(r, g, b))

    final_data = [item for sublist in data_set for item in sublist]

    # mean = np.mean(final_data)
    mean = (sum(final_data) / (SAMPLES * NUM_OF_PLOTS))

    v = [((x - mean) ** 2) for x in final_data]
    # variance = np.var(final_data)
    variance = sum(v) / (SAMPLES * NUM_OF_PLOTS)

    legend_data.append("mean: " + str(round(mean, 2)) + "  variance: " + str(round(variance, 2)))
    r, g, b = np.random.sample(3)
    sns.distplot(final_data, kde=True, hist=True, color=(r, g, b))
    axes.axvline(mean, color=(r, g, b), linestyle='--')
    plt.legend(legend_data, bbox_to_anchor=(0.6, 1))
    plt.show()


plot()
