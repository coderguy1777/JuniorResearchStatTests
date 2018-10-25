import pandas as pd
import matplotlib as plt
from scipy.stats import stats

dataset = pd.read_csv("VectorArrowDirection - Quasistatic Magnetic Field Vector Arrows Data for Graph.csv")
dataset.describe()