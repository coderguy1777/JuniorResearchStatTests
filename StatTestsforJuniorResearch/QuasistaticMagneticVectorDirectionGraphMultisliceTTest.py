import pandas as pd
import matplotlib as plt
from scipy.stats import stats

dataset = pd.read_csv("MultiSliceDataFromQSField - Quasistatic Magnetic Field Vector Direction Graph Multislice Data.csv")
dataset.describe()