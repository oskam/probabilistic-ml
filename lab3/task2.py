import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


DATA_TYPE = "wine"

def plot(data_type):

    if data_type == "wine":
        path = "lab3/datasets/wine.data"
        df = pd.read_csv(path)
        class_column = 11
        y = df[df.columns[class_column]]
        X = df.drop(columns=df.columns[class_column])
        # scatter_axes_histograms(3, 4, df)
        # sns.pairplot(df, hue=df.columns[class_column])
        scatter_diagonal_histogram(df, class_column)

    elif data_type == "yeast":
        path = "lab3/datasets/yeast.data"
        df = pd.read_csv(path)
        df = df.drop(columns=df.columns[0])
        class_column = 8
        y = df[df.columns[class_column]]
        X = df.drop(columns=df.columns[class_column])
        # scatter_axes_histograms(4, 5, df)
        # sns.pairplot(df, hue=df.columns[class_column])
        # plt.show()

def scatter_axes_histograms(x, y, df):
    g = sns.jointplot(x=df.columns[x], y=df.columns[y], data=df)
    plt.show()

def scatter_diagonal_histogram(df, class_column):
    g = sns.PairGrid(df, hue=df.columns[class_column])
    g = g.map_diag(plt.hist, edgecolor="w")
    g = g.map_offdiag(plt.scatter, edgecolor="w", s=40)
    g = g.add_legend()
    plt.show()

# print(X.head())
# print(y.head())

plot(DATA_TYPE)