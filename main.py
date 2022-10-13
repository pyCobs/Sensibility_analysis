import pandas as pd
import numpy as np
from numpy import ceil
import matplotlib.pyplot as plt
from math import sqrt

from error_bar import error_bar

# le but de ce script
# data
data = pd.read_csv("Data/Source/T0_VGR.1.csv", sep=";")

# colonne que je veux prédire
predict = "Cat_T0 VGR"

# moyenne et écart-type
error_bar(data, predict)
