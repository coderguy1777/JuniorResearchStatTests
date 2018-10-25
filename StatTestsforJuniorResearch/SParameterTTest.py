import pandas as pd
import matplotlib as plt
from scipy.stats import stats

dataset = pd.read_csv("SParameter Data - S Parameter Graph 1D Data.csv")
dataset.describe()