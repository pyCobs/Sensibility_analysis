import numpy as np
from numpy import ceil
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt


def error_bar(data, predict):

    # données d'entrée de mon dataframe
    columns = list(data.columns)
    columns.remove(predict)

    # nombre d'éléments de sortie différents
    n_predict = len(data[predict].unique())

    # les différentes valeurs de sortie
    value_predict = data[predict].unique()

    # création d'un dataframe par valeur à prédire
    df = []
    for n in range(n_predict):
        df.append(data[data[predict] == value_predict[n]])

    # unpivot chaque df
    df_unpivot = [pd.melt(df[n], value_vars=columns) for n in range(n_predict)]

    # Groupby the variable column using aggregate
    # value of mean and std
    qual = [df_unpivot[n].groupby('variable').agg([np.mean, np.std]) for n in range(n_predict)]
    score = [qual[n]['value'] for n in range(n_predict)]

    # nombre de colonnes nécessaire pour le plot
    n_sqrt = int(ceil(sqrt(n_predict)))

    # nombre de lignes
    n_ligne = int(ceil(n_predict / n_sqrt))

    # checking for results
    fig, axs = plt.subplots(n_ligne, n_sqrt, sharex=True, sharey=True)

    for n in range(n_predict):
        ligne = int(n // n_sqrt)
        colonne = int((n % n_sqrt))
        score[n].plot(kind="barh", y="mean", legend=False,
                      title="Score : " + str(value_predict[n]), xerr="std", ax=axs[ligne, colonne], xlim=(0, 4),
                      ylim=(0, 4))

    plt.show()