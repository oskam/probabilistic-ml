import pandas as pd
import numpy as np
from pandas import plotting
import seaborn as sns
import matplotlib.pyplot as plt


DATA_TYPE = "HTRU"

def plot(data_type):

    if data_type == "wine":
        path = "lab3/datasets/wine.data"
        df = pd.read_csv(path)
        class_column = 11
        y = df[df.columns[class_column]]
        X = df.drop(columns=df.columns[class_column])
        # correlation(df)
        # scatter_axes_histograms(3, 4, df)
        scatter_diagonal_histogram(df, class_column)
        # sns.pairplot(df, hue=df.columns[class_column])
        # scatter_diagonal_histogram(df, class_column)

        # pd.plotting.scatter_matrix(df, alpha=0.3, figsize=(14, 8), diagonal='kde')
        # plt.show()
        # sns.pairplot(df)

        # f, ax = plt.subplots(figsize=(10, 8))
        # corr = df.corr()
        # sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool), cmap=sns.diverging_palette(220, 10, as_cmap=True),
        #             square=True, ax=ax)
        # plt.show()


    elif data_type == "yeast":
        path = "lab3/datasets/yeast.data"
        df = pd.read_csv(path)
        df = df.drop(columns=df.columns[0])
        class_column = 8
        y = df[df.columns[class_column]]
        X = df.drop(columns=df.columns[class_column])
        # correlation(df)
        scatter_axes_histograms(4, 5, df)
        # sns.pairplot(df, hue=df.columns[class_column])
        # plt.show()

    elif data_type == "diabetes":
        path = "lab3/datasets/diabetes.data"
        df = pd.read_csv(path)
        class_column = 19
        y = df[df.columns[class_column]]
        X = df.drop(columns=df.columns[class_column])
        correlation(df)
        # scatter_axes_histograms(4, 5, df)

    elif data_type == "HTRU":
        path = "lab3/datasets/HTRU_2.csv"
        df = pd.read_csv(path)
        class_column = 8
        y = df[df.columns[class_column]]
        X = df.drop(columns=df.columns[class_column])
        correlation(df)
        # scatter_axes_histograms(4, 5, df)



def scatter_axes_histograms(x, y, df):
    g = sns.jointplot(x=df.columns[x], y=df.columns[y], data=df)
    plt.show()
#

def scatter_diagonal_histogram(df, class_column):
    g = sns.PairGrid(df, hue=df.columns[class_column])
    g = g.map_diag(plt.hist, edgecolor="w")
    g = g.map_offdiag(plt.scatter, edgecolor="w", s=40)
    g = g.add_legend()
    plt.show()



def correlation(df):
    # Compute the correlation matrix
    # corr = df.corr()
    corr = df.corr()


    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, annot=True,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.show()


def covariance(df):
    pass

# print(X.head())
# print(y.head())

plot(DATA_TYPE)