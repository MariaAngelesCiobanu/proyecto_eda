import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_graph(df: pd.DataFrame) -> None:

    plt.figure(figsize=(8,5))

    sns.countplot(data=df, x="type")

    plt.title("Movies vs TV Shows on Netflix")
    plt.xlabel("Content Type")
    plt.ylabel("Count")

    plt.show()
